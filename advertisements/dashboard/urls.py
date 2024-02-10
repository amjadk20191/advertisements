from django.urls import path,include
from rest_framework import routers
from .views import activeusertouseViewsets,planViewsets,connect_with_usViewsets, opinionViewsets,activeadvertisementViewsets ,complaintsViewsets,country,advertisementViewsets,pendingadvertisementViewsets,yemenpendingadvertisementViewsets

router = routers.DefaultRouter()
router.register(r'opinions', opinionViewsets, basename="opinion")
router.register(r'active-user', activeusertouseViewsets, basename="active-user")
router.register(r'complaints', complaintsViewsets, basename="complaints")
router.register(r'advertisement', advertisementViewsets, basename="advertisement")
router.register(r'active-advertisement', activeadvertisementViewsets, basename="active-advertisement")
router.register(r'pending-advertisement', pendingadvertisementViewsets, basename="pending-advertisement")
router.register(r'yemen-pending-advertisement', yemenpendingadvertisementViewsets, basename="yemen-pending-advertisement")
router.register(r'connect', connect_with_usViewsets, basename="connect")
router.register(r'plan', planViewsets, basename="plan")

urlpatterns = [

    path('', include(router.urls)),
    path('user-country/', country.as_view(), name="country"),




]