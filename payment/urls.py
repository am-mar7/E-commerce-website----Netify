from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkout/<str:name>/<int:price>/<str:price_id>/', views.checkout, name='checkout'),    
    path('create-checkout-session/', views.create_checkout_session, name='checkout_session'),
    path('payment/success/', views.success, name='success'),
    path('payment/cancel/', views.cancel, name='cancel'),
    path('create-payment/', views.create_checkout_session, name='save_UserPayment'),
]
