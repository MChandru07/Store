# Simple E-commerce Store (Django + HTML/CSS/JS)

## Features
- Product listing + product detail pages
- Session-based shopping cart
- Checkout creates an `Order` + `OrderItem`s
- User registration/login (Django auth)
- Order detail page (per-user)

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Create a few products (optional):
   ```bash
   python manage.py shell
   ```
   and run:
 ```python
      from shop.models import Product
      Product.objects.create(name='Keyboard', description='Mechanical keyboard', price=49.99, image_url='')
      Product.objects.create(name='Mouse', description='Wireless mouse', price=19.99, image_url='')
      Product.objects.create(name='Headphones', description='Noise cancelling', price=79.99, image_url='')
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```
   ---
   localhost8000
   
## URLs
- Home / product listing: `/`
- Product detail: `/product/<id>/`
- Cart: `/cart/`
- Add/update/remove cart: `/cart/add/`, `/cart/update/`, `/cart/remove/`
- Signup: `/signup/`
- Login/Logout: `/accounts/login/` and `/accounts/logout/`
- Checkout: `/checkout/`
- Order detail: `/orders/<order_id>/`

## run commend
---
python manage.py runserver 8000
---
----# CodeAlpha_E-commerceStore

