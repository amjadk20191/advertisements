
from .models import opinion,complaints,connect_with_us
from rest_framework import generics,viewsets,views
from .serializers import UserpayImageSerializer,opinionCreateSerializer, complaintsCreateSerializer,connect_with_usCreateSerializer
from dashboard.serializers import planSerializer
from dashboard.models import plan
from core.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException


class UserpayImage(generics.UpdateAPIView):
    http_method_names=['patch',]

    serializer_class = UserpayImageSerializer
    queryset=User.objects.only('Money_transfer_image','plan','pending_subscribe')




    def get_object(self):
        phone=self.request.data.pop('phone',None)
        if phone is None:
                raise APIException({"phone": "you have to enter phone number"})



        try:
                user=User.objects.get(phone=phone)
        except:
                user=User.objects.create(phone=phone,is_active=False,group='user')

        return user

    
    



class planList(generics.ListAPIView):
    queryset = plan.objects.all()
    serializer_class = planSerializer



class opinionCreate(generics.ListCreateAPIView):
    serializer_class = opinionCreateSerializer
    def get_queryset(self):
        if self.request.method == 'GET':
         self.queryset = opinion.objects.only('description').filter(active=True)
        if self.request.method == 'PATCH':
         self.queryset = opinion.objects.filter(active=True)
 

        return super().get_queryset()




class complaintsCreate(generics.CreateAPIView):
    queryset = complaints.objects.all()
    serializer_class = complaintsCreateSerializer



class connect_with_usCreate(generics.CreateAPIView):
    queryset = connect_with_us.objects.all()
    serializer_class = connect_with_usCreateSerializer