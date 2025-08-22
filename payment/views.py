from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import UserPayment
from django.http import JsonResponse


stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request, name, price, price_id):
    stripe_price = int(float(price) * 100)
    return render(request, 'payment/checkout.html', {
        'name': name,
        'price': price,
        'price_id': price_id,
        'stripe_price': stripe_price,
        'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY,
    })

@csrf_exempt
def create_checkout_session(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip")
        price = request.POST.get("price")
        name = request.POST.get("name")
        price_id = request.POST.get("price_id")

        user_payment = UserPayment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=phone,
            address=address,
            city=city,
            zip_code=zip_code,
            price_id=price_id,
            has_paid=False
        )

        YOUR_DOMAIN = "http://127.0.0.1:8000"
        try:
            stripe_price = int(float(price) * 100) + 6000
        except Exception as e:
            return JsonResponse({"error": f"Invalid price value: {price}"}, status=400)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': stripe_price, 
                        'product_data': {
                            'name': name or "Website Service",
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/payment/success/',
            cancel_url=YOUR_DOMAIN + '/payment/cancel/',
        )

        return redirect(checkout_session.url)
    else:
        return redirect('home')


def success(request):
    return render(request, "payment/success.html")


def cancel(request):
    return render(request, "payment/cancel.html")
