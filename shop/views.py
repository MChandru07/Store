import json
from decimal import Decimal

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt    
from .models import Order, OrderItem, Product 


CART_SESSION_KEY = "cart"


def _ensure_order_belongs_to_user(request, order_id: int) -> Order:
    return get_object_or_404(Order, id=order_id, user=request.user)



def _get_cart(session):
    return session.get(CART_SESSION_KEY, {})


def _set_cart(session, cart):
    session[CART_SESSION_KEY] = cart
    session.modified = True


def _cart_totals(cart):
    subtotal = Decimal("0.00")
    for product_id_str, qty in cart.items():
        product = Product.objects.filter(id=int(product_id_str)).first()
        if not product:
            continue
        subtotal += product.price * int(qty)

    tax = subtotal * Decimal("0.0")
    total = subtotal + tax
    return subtotal, tax, total


@require_GET
def product_list(request):
    products = Product.objects.all().order_by("id")
    return render(request, "shop/product_list.html", {"products": products})


@require_GET
def product_detail(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "shop/product_detail.html", {"product": product})


@require_GET
def cart_view(request):
    cart = _get_cart(request.session)
    product_ids = [int(pid) for pid in cart.keys()]
    products = Product.objects.filter(id__in=product_ids)

    items = []
    subtotal = Decimal("0.00")
    for p in products:
        qty = int(cart.get(str(p.id), 0))
        if qty <= 0:
            continue
        line_total = p.price * qty
        subtotal += line_total
        items.append({"product": p, "qty": qty, "line_total": line_total})

    tax = Decimal("0.00")
    total = subtotal + tax

    return render(
        request,
        "shop/cart.html",
        {
            "items": items,
            "subtotal": subtotal,
            "tax": tax,
            "total": total,
        },
    )


@require_POST
def cart_add(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
        product_id = int(payload["product_id"])
        quantity = int(payload.get("quantity", 1))
    except Exception:
        return JsonResponse({"ok": False, "error": "Invalid payload"}, status=400)

    if quantity <= 0:
        quantity = 1

    product = get_object_or_404(Product, id=product_id)

    cart = _get_cart(request.session)
    pid = str(product.id)
    cart[pid] = int(cart.get(pid, 0)) + quantity
    _set_cart(request.session, cart)

    return JsonResponse({"ok": True, "cart": cart})


@require_POST
def cart_update(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
        product_id = int(payload["product_id"])
        quantity = int(payload.get("quantity", 1))
    except Exception:
        return JsonResponse({"ok": False, "error": "Invalid payload"}, status=400)

    cart = _get_cart(request.session)
    pid = str(product_id)

    if quantity <= 0:
        cart.pop(pid, None)
    else:
        # Validate product exists
        get_object_or_404(Product, id=product_id)
        cart[pid] = quantity

    _set_cart(request.session, cart)
    return JsonResponse({"ok": True, "cart": cart})


@require_POST
def cart_remove(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
        product_id = int(payload["product_id"])
    except Exception:
        return JsonResponse({"ok": False, "error": "Invalid payload"}, status=400)

    cart = _get_cart(request.session)
    cart.pop(str(product_id), None)
    _set_cart(request.session, cart)
    return JsonResponse({"ok": True, "cart": cart})


@login_required
@require_GET
def checkout(request):
    cart = _get_cart(request.session)
    if not cart:
        return redirect("product_list")

    # Build items
    product_ids = [int(pid) for pid in cart.keys()]
    products = {p.id: p for p in Product.objects.filter(id__in=product_ids)}

    subtotal = Decimal("0.00")
    items_payload = []
    for pid_str, qty in cart.items():
        pid = int(pid_str)
        qty = int(qty)
        product = products.get(pid)
        if not product or qty <= 0:
            continue
        subtotal += product.price * qty
        items_payload.append((product, qty))

    if not items_payload:
        return redirect("product_list")

    tax = Decimal("0.00")
    total = subtotal + tax

    order = Order.objects.create(
        user=request.user,
        status=Order.Status.PAID,
        subtotal=subtotal,
        tax=tax,
        total=total,
    )

    for product, qty in items_payload:
        OrderItem.objects.create(order=order, product=product, quantity=qty, unit_price=product.price)

    # Clear cart
    _set_cart(request.session, {})

    return redirect("order_detail", order_id=order.id)


@login_required
@require_GET
def order_detail(request, order_id: int):
    order = _ensure_order_belongs_to_user(request, order_id)
    return render(
        request,
        "shop/order_detail.html",
        {
            "order": order,
            "items": order.items.select_related("product").all(),
        },
    )


@login_required
@require_GET
def payment_method(request, order_id: int):
    order = _ensure_order_belongs_to_user(request, order_id)
    return render(request, "shop/payment_method.html", {"order": order})


@login_required
@require_GET
def pay_upi(request, order_id: int):
    order = _ensure_order_belongs_to_user(request, order_id)
    upi_id = "support@novamart.example"
    amount = f"{order.total}"
    name = "NovaMart"
    note = f"Order #{order.id}"
    upi_intent_url = (
        "upi://pay?pa="
        + upi_id
        + "&pn="
        + name
        + "&am="
        + amount
        + "&cu=INR"
        + "&tn="
        + note
    )
    return render(
        request,
        "shop/payments_upi.html",
        {"order": order, "upi_id": upi_id, "upi_intent_url": upi_intent_url},
    )


@login_required
@require_GET
def pay_debit_card(request, order_id: int):
    order = _ensure_order_belongs_to_user(request, order_id)
    return render(request, "shop/debit_card.html", {"order": order})


@login_required
@require_GET
def pay_credit_card(request, order_id: int):
    order = _ensure_order_belongs_to_user(request, order_id)
    return render(request, "shop/credit_card.html", {"order": order})


@login_required
@require_POST
def mark_order_paid(request, order_id: int):
    order = _ensure_order_belongs_to_user(request, order_id)
    order.status = Order.Status.PAID
    order.save(update_fields=["status"])
    return redirect("order_detail", order_id=order.id)


@require_GET
def signup(request):

    if request.user.is_authenticated:
        return redirect("product_list")
    form = UserCreationForm()
    return render(request, "shop/signup.html", {"form": form})


@require_POST
def signup_post(request):

    if request.user.is_authenticated:
        return redirect("product_list")
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("product_list")
    return render(request, "shop/signup.html", {"form": form})


