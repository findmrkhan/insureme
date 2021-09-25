from django.urls import path
from .views import CustomerCreateView, QuoteCreateView, PolicyListView, PolicyDetailView, PolicyHistoryView, QuoteUpdateView

urlpatterns = [
    path('v1/create_customer/', CustomerCreateView.as_view(), name='customer_create'),
    #path('v1/quote/', QuoteListView.as_view(), name='quote_list'),
    path('v1/quote/', QuoteCreateView.as_view(), name='quote_create'),
    path('v1/quote/<int:pk>/', QuoteUpdateView.as_view(), name='quote_update'),
    path('v1/policies/', PolicyListView.as_view(), name='policy-list'),
    path('v1/policies/<int:pk>/history/', PolicyHistoryView.as_view(), name='policy-history'),
    path('v1/policies/<int:pk>/', PolicyDetailView.as_view(), name='policy-detail'),


]