

from django.urls import path
from .views import PayPalWebhookView

urlpatterns = [
    path('webhook/', PayPalWebhookView.as_view(), name='webhook'),
    
]