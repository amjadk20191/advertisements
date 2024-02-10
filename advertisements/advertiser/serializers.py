from rest_framework import serializers
from core.models import User
from .models import advertisement
from advertisements.settings import timezone
import os

from drf_extra_fields.fields import Base64ImageField
import datetime





class advertiserCreateSerializer(serializers.ModelSerializer):
   
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['name','phone','password']

    def validate(self, data):
            password = data.get('password',None)
            if password is None:
                     raise serializers.ValidationError({"password":"miss required field"})
            name = data.get('name',None)
            if name is None:
                     raise serializers.ValidationError({"name":"miss required field"})
            return data
 
    
    
    def create(self, validated_data):

       
            validated_data['group']='advertiser'
            
            data=super().create(validated_data)
            
            return data
        

class advertisementSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = advertisement
        fields = ['pk','name','country','description','refuse_text','date_of_start','date_of_end','price','URL','cative','active_to_see']
        extra_kwargs = {'cative': {'read_only': True},
                        'refuse_text': {'read_only': True},
                        'active_to_see': {'read_only': True},
                        }
        
    
    def create(self, validated_data):
        if (validated_data['date_of_start'] > validated_data['date_of_end'])or(validated_data['date_of_start'] < datetime.datetime.now(timezone).date()):
            
          raise serializers.ValidationError(detail={"detail":"eror in date"})


        data=advertisement.objects.create(user=User(pk=self.context['request'].user['pk']),**validated_data)

        
        return data
class addimageadvertisementSerializer(serializers.ModelSerializer):
    image=Base64ImageField()

    class Meta:
        model = advertisement
        fields = ['pk','image']

    
    def validate(self, data):
            image = data.get('image',None)
            if image is None:
                     raise serializers.ValidationError({"image":"miss required field"})
            return data
 
    

    def update(self, instance, validated_data):
         try:    
            if 'image' in validated_data :  
                old_image_path=instance.image.path
                if os.path.exists(old_image_path):
        
                        os.remove(old_image_path)
         except:
              pass
         return super().update( instance, validated_data)    
        
    
