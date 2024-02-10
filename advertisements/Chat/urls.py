from django.urls import path,include
from rest_framework import routers
from .views import redirectTO ,chatTelgram
router = routers.DefaultRouter()
urlpatterns = [
   
    path('', include(router.urls)),
    path('redirectTO/<int:pk>/<str:uuid>', redirectTO.as_view(), name="redirectTO"),
    path('chattelgram/', chatTelgram.as_view(), name="chattelgram"),


]