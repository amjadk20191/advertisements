from rest_framework import serializers
from .models import opinion, complaints,connect_with_us
from core.models import User

from drf_extra_fields.fields import Base64ImageField
import os



class UserpayImageSerializer(serializers.ModelSerializer):
    Money_transfer_image=Base64ImageField()


    class Meta:
        model = User
        fields = ['Money_transfer_image','phone','plan']
    def validate(self, data):
            Money_transfer_image = data.get('Money_transfer_image',None)
            plan = data.get('plan',None)
            if plan is None:
                     raise serializers.ValidationError({"plan":"miss required field"})

            if Money_transfer_image is None:
                 raise serializers.ValidationError({"Money_transfer_image":"miss required field"})
            return data
                 
     
    def update(self, instance, validated_data):
        try:    
            if 'Money_transfer_image' in validated_data :  
                old_image_path=instance.Money_transfer_image.path
                if os.path.exists(old_image_path):
        
                        os.remove(old_image_path)
        except:
              pass
        
        validated_data['pending_subscribe'] = True

        return super().update( instance, validated_data)    
        



class opinionCreateSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = opinion
        fields = ['pk','description']



class complaintsCreateSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = complaints
        fields = ['pk','description','email','phone']
class connect_with_usCreateSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = connect_with_us
        fields = ['pk','description','email','phone']