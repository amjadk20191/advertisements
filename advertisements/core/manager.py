
from django.contrib.auth.base_user import BaseUserManager



from phonenumbers import  NumberParseException
from rest_framework.exceptions import APIException
import re


from phone_iso3166.country import phone_country 
import pycountry
from advertisements.settings import countries
import os
class UserManager(BaseUserManager):
    use_in_migrations = True



    def delete(self, *args, **kwargs):
        try:
           image_path = self.Money_transfer_image.path
           if os.path.exists(image_path):
               os.remove(image_path)
        except:
            pass

        
        return super().delete(*args, **kwargs)
        


    def create(self, password=None, **extra_fields):





        try:

        
            pattern = r'^\+\d{3,15}$'

            if not re.match(pattern, extra_fields['phone']):
             raise APIException(detail={"detail":"phone number is unvalid"})
            parsed_number = phone_country(extra_fields['phone'])

         
        except :
             raise APIException(detail={"detail":"phone number is unvalid"})



        
        
        try:
            extra_fields['country'] = countries[pycountry.countries.get(alpha_2 = parsed_number).name]
        except:
             raise APIException(detail={"detail":"not allow"})



   

 
        user = self.model(**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user






    def create_for_chat(self, password=None, **extra_fields):
        try:
            pattern = r'^\+\d{3,15}$'

            if not re.match(pattern, extra_fields['phone']):
             return None
            parsed_number = phone_country(extra_fields['phone'])

         
        except :
            return None




        
        
        try:
            extra_fields['country'] = countries[pycountry.countries.get(alpha_2 = parsed_number).name]
        except:
           return "not supported"



   

 
        user = self.model(**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user





 



    def create_superuser(self, password, **extra_fields):
        try:
            pattern = r'^\+\d{3,15}$'

            if not re.match(pattern, extra_fields['phone']):
                raise APIException(detail={"detail":"phone number is unvalid"})
            parsed_number = phone_country(extra_fields['phone'])

        
        except NumberParseException:
             raise APIException(detail={"detail":"phone number is unvalid"})



        
        
        try:
            extra_fields['country'] = countries[pycountry.countries.get(alpha_2 = parsed_number).name]
        except:
             raise APIException(detail={"detail":"not allow"})


        user = self.model(**extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.active = True
        user.group='admin'
        user.save(using=self._db)

        return user



    def update(self, user_id, **kwargs):

           


            user = self.get(id=user_id)

            for attr, value in kwargs.items():
                setattr(user, attr, value)
            user.set_password(kwargs['password'])

            user.save(using=self._db)

            return user
