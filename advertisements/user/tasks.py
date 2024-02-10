from time import sleep
from celery import shared_task
from core.models import User
import datetime
from django.db.models import Q
from advertiser.models import advertisement
from django.db.models import Avg,Max
from advertisements.settings import timezone
@shared_task
def dailyTask ():

    User.objects.only('use').filter(Q(dateOfEnd__lt=datetime.datetime.now(timezone).date())&Q(use=True)&Q(Q(group='advertiser')|Q(group='user'))).update(use=False)
    advertisement.objects.only('active_to_see').filter(Q(date_of_end__lt=datetime.datetime.now(timezone).date())).delete()
  
    avg=advertisement.objects.values('country').annotate(price=Avg('price')).order_by('country') 
        
    max=advertisement.objects.values('country').annotate(price=Max('price')).order_by('country')
 
    if max is None and avg is None:
        for i in range(len(max)):

                
                
                
                if not max[i]['price']==avg[i]['price']:
                        dif_num=max[i]['price']-avg[i]['price']
                        min_num=min(dif_num,max[i]['price']) 
                        max_num=max(dif_num,max[i]['price'])
                        num=max_num+min_num/2
                        

                        
                        advertisement.objects.only('important_group').filter(country=max[i]['country'],price__gte=avg[i]['price']).update(important_group=1)
                        advertisement.objects.only('important_group').filter(country=max[i]['country'],price__gt=num ).update(important_group=2)





