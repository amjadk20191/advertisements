from django.urls import path,include
from rest_framework import routers
from .views import complaintsCreate,opinionCreate,connect_with_usCreate,planList,UserpayImage

router = routers.DefaultRouter()
# router.register(r'by-image', UserpayImage, basename="by-image")

urlpatterns = [

    path('', include(router.urls)),
    path('complaint/', complaintsCreate.as_view(), name="complaints-Creat"),
    path('opinion/', opinionCreate.as_view(), name="opinion-Create"),
    path('connect/', connect_with_usCreate.as_view(), name="connect_with_us"),
    path('by-image/', UserpayImage.as_view(), name="by-image"),
    path('plan/', planList.as_view(), name="plan"),

    


]