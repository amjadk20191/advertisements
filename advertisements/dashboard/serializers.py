from rest_framework import serializers
from user.models import opinion, complaints
from core.models import User
from advertiser.models import advertisement
import datetime
from .models import plan
import os
import datetime
from django.conf import settings
from advertisements.settings import timezone



class activeUserSerializer(serializers.ModelSerializer):
    price=serializers.DecimalField(read_only=True,max_digits=20,decimal_places=2)
    number_of_day=serializers.IntegerField()
    name=serializers.CharField(read_only=True)
    Money_transfer_image=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['pk','Money_transfer_image','phone','country','name','number_of_day','price','use']
        extra_kwargs = {
                        'phone': {'read_only': True},
                        'use': {'write_only': True},
                        'country': {'read_only': True}
                       }
             
    def update(self, instance, validated_data):
        
            
          validated_data['pending_subscribe'] = False
          validated_data['dateOfEnd'] =   datetime.datetime.now(timezone).date()+datetime.timedelta(days=validated_data['number_of_day']) 


          return super().update( instance, validated_data)    
            
    def validate(self, data):
        use = data.get('use',None)
        if use is None:
                    raise serializers.ValidationError({"use":"miss required field"})
        return data
    def get_Money_transfer_image(self, obj):

        request = self.context.get('request')

        if isinstance(obj,User):

            return request.build_absolute_uri('/') + os.path.join(settings.MEDIA_URL[1:],str(obj.Money_transfer_image) )   
        
        if isinstance(obj,dict) and obj['Money_transfer_image']:


  
            return request.build_absolute_uri('/')+ os.path.join(settings.MEDIA_URL[1:],obj['Money_transfer_image'] )   





class planSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = plan
        fields = ['pk','name','number_of_day','price']

    







class opinionSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = opinion
        fields = ['pk','description','active']
        extra_kwargs = {'description': {'read_only': True}                        }
 
    def validate(self, data):
            active = data.get('active',None)
            if active is None:
                     raise serializers.ValidationError({"active":"miss required field"})
            return data
    
    






class advertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = advertisement
        fields = ['pk','name','country','description','URL','active_to_see','price','date_of_end','date_of_start']
 
    def validate(self, data):
            price = data.get('price',None)
            if price is None:
                     raise serializers.ValidationError({"price":"miss required field"})
            return data
    
    
    
    def create(self, validated_data):
        if (validated_data['date_of_start'] > validated_data['date_of_end'])or(validated_data['date_of_start'] < datetime.datetime.now(timezone).date()):
            
           raise serializers.ValidationError(detail={"detail":"eror in date"})
        delta =validated_data['date_of_end'] - validated_data['date_of_start']
        validated_data['important'] = validated_data['price']/delta.days
      

        data=advertisement.objects.create(user=User(pk=self.context['request'].user['pk']),**validated_data)

        
        return data

       

class pendingadvertisementSerializer(serializers.ModelSerializer):
    username=serializers.CharField(read_only=True)
    phone=serializers.CharField(read_only=True)
    class Meta:
        model = advertisement
        fields = ['pk','username','phone','name','country','description','URL','cative','price','refuse_text','date_of_end','date_of_start']
        extra_kwargs = {'name': {'read_only': True},
                        'country': {'read_only': True},
                        'description': {'read_only': True},
                        'date_of_end': {'read_only': True},
                        'date_of_start': {'read_only': True},
                        'URL': {'read_only': True},
                       }

    def validate_cative(self, value):
          if  value is None:
                raise serializers.ValidationError("is required")
          return value
    
    def validate(self, data):
            price = data.get('price',None)
            refuse_text = data.get('refuse_text',None)
            cative = data.get('cative',None)
            if cative is None:
                raise serializers.ValidationError({"cative" : "you have to enter the cative"})

                 
            
            if not cative and refuse_text is None:
                raise serializers.ValidationError({"refuse_text" : "you have to enter the refuse text"})
            
            if  cative and price is None :
                raise serializers.ValidationError({"price" :"you have to enter the price"})
            
            return data
            
    def update(self, instance, validated_data):
          if 'price' in validated_data:
            
                delta =instance.date_of_end - instance.date_of_start
                validated_data['important'] = validated_data['price']/delta.days

          return super().update( instance, validated_data)    
            
    




class yemenPendingadvertisementSerializer(serializers.ModelSerializer):
    username=serializers.CharField(read_only=True)
    phone=serializers.CharField(read_only=True)
    image=serializers.SerializerMethodField(read_only=True)


   

    class Meta:
        model = advertisement
        fields = ['pk','username','phone','name','country','image','description','URL','price','date_of_end','date_of_start','active_to_see']
        extra_kwargs = {'name': {'read_only': True},
                        'country': {'read_only': True},
                        'description': {'read_only': True},
                        'date_of_end': {'read_only': True},
                        'date_of_start': {'read_only': True},
                        'image': {'read_only': True},
                        'price': {'read_only': True},

                        'URL': {'read_only': True}
                        
                        
                        }
    def get_image(self, obj):

        request = self.context.get('request')

        if isinstance(obj,advertisement):

            return request.build_absolute_uri('/') +os.path.join(settings.MEDIA_URL[1:],str(obj.image) )    
        
        if isinstance(obj,dict) and obj['image']:
            request = self.context.get('request')


  
            return request.build_absolute_uri('/') +os.path.join(settings.MEDIA_URL[1:],obj['image'] )  
        
        return None

    def validate(self, data):
            active_to_see = data.get('active_to_see',None)
            if active_to_see is None:
                     raise serializers.ValidationError({"active_to_see":"miss required field"})
            return data
 

class activedvertisementSerializer(serializers.ModelSerializer):
    username=serializers.CharField(read_only=True)
    phone=serializers.CharField(read_only=True)

   

    class Meta:
        model = advertisement
        fields = ['pk','username','phone','name','country','description','URL','price','date_of_end','date_of_start','active_to_see']
        extra_kwargs = {'name': {'read_only': True},
                        'country': {'read_only': True},
                        'description': {'read_only': True},
                        'date_of_end': {'read_only': True},
                        'price': {'read_only': True},
                        'date_of_start': {'read_only': True},
                        'active_to_see': {'read_only': True},
                        'URL': {'read_only': True}                       
                        
                        
                        }
                