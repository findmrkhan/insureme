from django.urls import path
from .views import CustomerCreateView

urlpatterns = [
    path('v1/create_customer/', CustomerCreateView.as_view(), name='customer_create'),
]