from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import admin
from django.urls import path, include

urlpatterns = [
    
    path("", views.product_list, name="product_list"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart_view, name="cart_view"),
    path("cart/add/", views.cart_add, name="cart_add"),
    path("cart/update/", views.cart_update, name="cart_update"),
    path("cart/remove/", views.cart_remove, name="cart_remove"),
    path("checkout/", views.checkout, name="checkout"),
    path("orders/<int:order_id>/", views.order_detail, name="order_detail"),

    path("orders/<int:order_id>/payment/", views.payment_method, name="payment_method"),
    path("orders/<int:order_id>/payment/upi/", views.pay_upi, name="pay_upi"),
    path("orders/<int:order_id>/payment/debit/", views.pay_debit_card, name="pay_debit_card"),
    path("orders/<int:order_id>/payment/credit/", views.pay_credit_card, name="pay_credit_card"),
    path("orders/<int:order_id>/payment/mark-paid/", views.mark_order_paid, name="mark_order_paid"),

    path("signup/", views.signup, name="signup"),
    path("signup/submit/", views.signup_post, name="signup_post"),

]
