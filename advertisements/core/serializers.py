from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from advertiser.models import advertisement



class TokenObtainPairSerializerNew(TokenObtainPairSerializer):
    def validate(self, attrs) :



         data= super().validate(attrs)
         data['phone'] = self.user.phone
         data['country'] = self.user.country
         data['type'] = self.user.group





         return data
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.name
        token['group'] = user.group

        return token
