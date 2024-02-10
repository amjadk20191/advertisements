from django.urls import path,include
from rest_framework import routers
from .views import advertiserCreat, advertisementViewsets,addimageadvertisementViewsets

router = routers.DefaultRouter()
router.register(r'advertisement', advertisementViewsets, basename="advertisement")
router.register(r'add-image', addimageadvertisementViewsets, basename="add-image")

urlpatterns = [
    path('', advertiserCreat.as_view(), name="advertiser-creat"),
    
    
    path('', include(router.urls)),

]