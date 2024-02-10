from django.shortcuts import render
from core.models import User
from rest_framework import generics,viewsets,views
from .serializers import advertiserCreateSerializer, advertisementSerializer,addimageadvertisementSerializer
from .models import advertisement
from .permissions import advertiseronly
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.db.models import Q
import unicodedata
import re
import datetime
import convert_numbers
from advertisements.settings import timezone

class advertiserCreat(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = advertiserCreateSerializer
    def post(self, request, *args, **kwargs):
        request.data._mutable = True
       
        data =request.data
        if not ("password" in data and "phone" in data and "name" in data):
             return Response({"detail": "error in json"}, status=status.HTTP_400_BAD_REQUEST)
        pattern = r'^\+\d{3,15}$'

        if not re.match(pattern, data['phone']):
              return Response({"detail":"phone number is unvalid"}, status=status.HTTP_400_BAD_REQUEST)


        numeral =convert_numbers.hindi_to_english(data['phone'][1:])
        numeral= str("+" + numeral)

        data.update({"phone":numeral})

        
        hashed_password = make_password(data['password'])
        if User.objects.filter(phone=numeral,group='user').update(group='advertiser',password=hashed_password,name=data['name']):

            
           
            return Response({"phone":numeral,
                             "name":data['name']}, status=status.HTTP_201_CREATED)
  
        else:
        
            return self.create(request, *args, **kwargs)




class advertisementViewsets(viewsets.ModelViewSet):
    http_method_names=['post','get','delete']
    serializer_class = advertisementSerializer
    permission_classes = [ advertiseronly]
    
    def get_queryset(self):
        if self.request.method == 'GET':
            self.queryset = advertisement.objects.values('pk','name','country','description','refuse_text','date_of_start','date_of_end','URL','cative','price','active_to_see').filter(Q(user__pk=self.request.user['pk'])&Q(Q(date_of_start__gte=datetime.datetime.now(timezone).date())|Q(Q(date_of_end__gte=datetime.datetime.now(timezone).date())&Q(active_to_see=True))))
        else:
                self.queryset = advertisement.objects.filter(Q(user__pk=self.request.user['pk'])&Q(Q(date_of_start__gte=datetime.datetime.now(timezone).date())|Q(Q(date_of_end__gte=datetime.datetime.now(timezone).date())&Q(active_to_see=True))))


        
        return super().get_queryset()




class addimageadvertisementViewsets(viewsets.ModelViewSet):
    http_method_names=['patch','get']

    serializer_class = addimageadvertisementSerializer
    permission_classes = [ advertiseronly]
    
    def get_queryset(self):
        self.queryset = advertisement.objects.only('image').filter(Q(user__pk=self.request.user['pk'])&Q(date_of_start__gte=datetime.datetime.now(timezone).date())&Q(cative=True))
        return super().get_queryset()


