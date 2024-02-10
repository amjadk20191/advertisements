
from datetime import datetime
import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin,AnonymousUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import  MinValueValidator
from dashboard.models import plan


from .manager import UserManager
class NewAnonymousUser(AnonymousUser):
        group=""



def upload_path(instance, filname):
    now = datetime.now()
    date_time = now.strftime("%m%d%Y%H%M%S")
    return '/'.join([ str(uuid.uuid4()) + str(date_time) + filname])


class User(AbstractBaseUser, PermissionsMixin):
    plan = models.ForeignKey(plan, on_delete=models.SET_NULL,blank=True, null=True)
    pending_subscribe=models.BooleanField(blank=True, default=False)

    phone=models.CharField(_('phone'), max_length=30,unique=True)
    country=models.CharField( max_length=30,blank=True, null=True)
    name=models.CharField( max_length=30,blank=True, null=True)

    number_of_free_message=models.IntegerField(blank=True,validators=[MinValueValidator(0)],default=0)

    dateOfEnd=models.DateField(blank=True, null=True)
    

    Money_transfer_image=models.FileField(upload_to=upload_path, blank=True, null=True)
    is_active = models.BooleanField(_('active'), default=True)
    active = models.BooleanField(_('active for chat'), default=False)
    use = models.BooleanField(_('using chat'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    group=models.CharField( max_length=30,blank=True)
    telgramID=models.CharField(max_length=50, null=True,blank=True)
    
    
    



    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')