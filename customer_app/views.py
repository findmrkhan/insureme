from rest_framework.generics import CreateAPIView
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.
class CustomerCreateView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

