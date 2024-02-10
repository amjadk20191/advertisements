import os 
from celery import Celery
   

os.environ.setdefault('DJANGO_SETTINGS_MODULE','advertisements.settings')
celery=Celery('advertisements')
celery.config_from_object('django.conf:settings',namespace='CELERY')
celery.autodiscover_tasks()