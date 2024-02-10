from django.shortcuts import render
from core.models import User
from rest_framework import generics,viewsets,views
from .serializers import activeUserSerializer, planSerializer, opinionSerializer,advertisementSerializer,pendingadvertisementSerializer,yemenPendingadvertisementSerializer,activedvertisementSerializer
from user.models import opinion,complaints,connect_with_us
from .permissions import adminonly
from advertiser.models import advertisement
from django.db.models import Q
import datetime
from user.serializers import connect_with_usCreateSerializer,complaintsCreateSerializer
from advertisements.settings import timezone

from rest_framework.response import Response
from core.models import User
from .models import plan
from django.db.models import F
import convert_numbers

from django.db.models import Count ,Value

class activeusertouseViewsets(viewsets.ModelViewSet):
    http_method_names=['get','patch']

    serializer_class = activeUserSerializer
    permission_classes = [ adminonly]
    
    def get_queryset(self):
            if self.request.method == 'GET':
       
                self.queryset = User.objects.select_related('plan').values('pk','Money_transfer_image','phone','country','plan__name','plan__number_of_day','plan__price').annotate(name=F('plan__name'),number_of_day=F('plan__number_of_day'),price=F('plan__price')).exclude(Money_transfer_image='').filter(Q(pending_subscribe=True)&Q(country="اليمن")&~Q(plan=None))
            if self.request.method == 'PATCH':
                self.queryset = User.objects.only('use','pending_subscribe','dateOfEnd').exclude(Money_transfer_image='').filter(Q(pending_subscribe=True)&Q(country="اليمن")&~Q(plan=None))

            return super().get_queryset()


class planViewsets(viewsets.ModelViewSet):
    http_method_names=['get','delete','patch','post']

    serializer_class = planSerializer
    queryset=plan.objects.all()
    permission_classes = [ adminonly]
    def post(self, request, *args, **kwargs):
        request.data._mutable = True
       
       

        request.data['number_of_day'] =convert_numbers.hindi_to_english(request.data['number_of_day'])
        request.data['price'] =convert_numbers.hindi_to_english(request.data['price'])
        
        return super().create(request, *args, **kwargs)

    






class  country (views.APIView):
    permission_classes = [ adminonly]


    def get(self, request, *args, **kwargs):
        
        return Response( User.objects.values('country').exclude(group='admin').annotate(count=Count('country')))

class opinionViewsets(viewsets.ModelViewSet):
    http_method_names=['get','delete','patch']

    serializer_class = opinionSerializer
    queryset=opinion.objects.all()

    
    permission_classes = [ adminonly]
    


class complaintsViewsets(viewsets.ModelViewSet):
    http_method_names=['get','delete']

    serializer_class = complaintsCreateSerializer
    queryset=complaints.objects.all()
    permission_classes = [ adminonly]
class connect_with_usViewsets(viewsets.ModelViewSet):
    http_method_names=['get','delete']

    serializer_class = connect_with_usCreateSerializer
    queryset=connect_with_us.objects.all()
    permission_classes = [ adminonly]
    
class advertisementViewsets(viewsets.ModelViewSet):
    http_method_names=['get','delete','patch','post']

    serializer_class = advertisementSerializer
    permission_classes = [ adminonly]
    
    def get_queryset(self):
        self.queryset = advertisement.objects.only('pk','name','country','description','URL','active_to_see','price','date_of_end','date_of_start').filter(Q(user__pk=self.request.user['pk'])&Q(Q(date_of_start__gte=datetime.datetime.now(timezone).date())|Q(Q(date_of_end__gte=datetime.datetime.now(timezone).date())&Q(active_to_see=True))))
        return super().get_queryset()



class pendingadvertisementViewsets(viewsets.ModelViewSet):
    http_method_names=['get','patch']

    serializer_class = pendingadvertisementSerializer
    permission_classes = [ adminonly]
    
    def get_queryset(self):
        if self.request.method == 'GET':
          self.queryset = advertisement.objects.select_related('user').values('pk','user__name','name','country','description','URL','cative','price','refuse_text','date_of_end','date_of_start','user__phone').annotate(username=F('user__name'),phone=F('user__phone')).exclude(user__group='admin').filter(Q(date_of_start__gte=datetime.datetime.now(timezone).date())&Q(cative=None))
        if self.request.method == 'PATCH':
            self.queryset = advertisement.objects.only('important','cative','price','refuse_text').exclude(user__group='admin').filter(Q(date_of_start__gte=datetime.datetime.now(timezone).date())&Q(cative=None))



        return super().get_queryset()
    def post(self, request, *args, **kwargs):
        request.data._mutable = True
       
 
        request.data['price'] =convert_numbers.hindi_to_english(request.data['price'])
        return super().create(request, *args, **kwargs)





class yemenpendingadvertisementViewsets(viewsets.ModelViewSet):
    http_method_names=['get','patch']

    serializer_class = yemenPendingadvertisementSerializer
    permission_classes = [ adminonly]
    
    def get_queryset(self):
            if self.request.method == 'GET':
       
                self.queryset = advertisement.objects.select_related('user').values('pk','user__name','name','country','description','URL','price','date_of_end','date_of_start','active_to_see','user__phone','image').annotate(username=F('user__name'),phone=F('user__phone')).exclude(image='').filter(Q(date_of_end__gte=datetime.datetime.now(timezone).date())&Q(cative=True)&Q(active_to_see=False)&Q(user__country="اليمن"))
            if self.request.method == 'PATCH':
                self.queryset = advertisement.objects.only('active_to_see').exclude(image='').filter(Q(date_of_end__gte=datetime.datetime.now(timezone).date())&Q(cative=True)&Q(active_to_see=False)&Q(user__country="اليمن"))

            return super().get_queryset()

class activeadvertisementViewsets(viewsets.ModelViewSet):
    http_method_names=['get']

    serializer_class = activedvertisementSerializer
    permission_classes = [ adminonly]
    
    def get_queryset(self):
             if self.request.method == 'GET':
                self.queryset = advertisement.objects.select_related('user').values('pk','user__name','name','country','description','URL','price','date_of_end','date_of_start','active_to_see','user__phone').annotate(username=F('user__name'),phone=F('user__phone')).filter(Q(date_of_end__gte=datetime.datetime.now(timezone).date())&Q(active_to_see=True))
           



             return super().get_queryset()


