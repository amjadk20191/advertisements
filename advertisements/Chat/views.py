from django.shortcuts import render
from rest_framework import generics,viewsets,views
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
import base64
from core.models import User
from advertiser.models import advertisement, seen_advertisement
from .utils import CustomThread
from .models import chat
from rest_framework.reverse import reverse
from django.db import IntegrityError
import requests
import openai
from django.forms.models import model_to_dict
import json
import datetime
from advertisements.settings import timezone
from advertisements import settings

from django.db.models import Avg,Max


        
      






class  redirectTO (views.APIView):


    def get(self, request, *args, **kwargs):
        pku=kwargs['pk']
        
      



        try:
            decoded_phone = base64.b64decode(kwargs['uuid'])
            decoded_phone = decoded_phone.decode('utf-8')
        except:
            return Response({"detail": "error"}, status=status.HTTP_400_BAD_REQUEST)
        user=User.objects.values('pk').filter(phone=decoded_phone).first()
        if user is None:
               return Response({"detail": "error in URL"}, status=status.HTTP_400_BAD_REQUEST)
        
        url=advertisement.objects.values('URL').filter(pk=pku).first()   
        if url is None:     
               return Response({"detail": "error in URL"}, status=status.HTTP_400_BAD_REQUEST)

        try:        
              seen_advertisement.objects.create(user=User(pk=user['pk']), advertisement=advertisement(pk=pku))
        except:
               pass
    


  
        

        return redirect (url['URL'])












      

def get_chat(id,userC):
      chats=[]
      all_chats=chat.objects.values('system_chat','user_chat').filter(user=id).order_by('-pk')[:3]#########
      for one_chat in all_chats:
            chats.append({"role":"user","content":one_chat['user_chat']})
            chats.append({"role":"assistant","content":one_chat['system_chat'].strip("\n").strip()})
      chats.append({"role":"user","content":userC})
      response=openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=chats)

      return response['choices'][0]['message']['content'] 



def send_message_T(chat_id,text):
       
              
              url=f'https://api.telegram.org/bot{settings.TokenTelgram}/sendMessage'
              payload={'chat_id':chat_id ,'text':text}
              keyboard = [[{
                            'text': 'ارسال الرقم الخاص بي',
                            'request_contact': True,
                            }]]

              payload = {
                     'chat_id': chat_id,
                     'text': text,
                     'reply_markup': {
                            'keyboard': keyboard,
                            'resize_keyboard': True,
                            'one_time_keyboard': True,
                     }
                     }
              requests.post(url, json=payload)



class  chatTelgram (views.APIView):
        def post(self, request, *args, **kwargs):
              data= request.data['message']
              try:
       
                     chat_id=data['chat']['id']
                     if "contact" in data:
                            phone=data['contact']['phone_number']
                            phone="+"+phone+"1"##########################################################

                            if User.objects.filter(phone=phone).update(telgramID=str(chat_id)):
                                   send_message_T(chat_id,"تم")
                                   return Response(status=status.HTTP_200_OK)
                            else:
                                   user=User.objects.create_for_chat(phone=phone,is_active=False,group='user',use=True,number_of_free_message=5,telgramID=str(chat_id))
                                   if user is None:
                                          send_message_T(chat_id,"خطأ في الرقم")
                                          return Response(status=status.HTTP_200_OK)
                                   if user =="not supported":
                                          send_message_T(chat_id,"غير مدعوم في الدولة الخاصة بك")
                                          return Response(status=status.HTTP_200_OK)
                                   else:
                                          send_message_T(chat_id,"تم")
                                          return Response(status=status.HTTP_200_OK)
                     user=User.objects.values('pk','active','number_of_free_message','country','phone').filter(telgramID=str(chat_id)).first()
                     if user is None:
                     
                            send_message_T(chat_id,"يرحى ارسال الرقم الخاص بك")
                            return Response(status=status.HTTP_200_OK)
                     text=data['text']
              except:
                    send_message_T(chat_id,"خطأ")
                    return Response(status=status.HTTP_200_OK)

              
              
              if user["active"]==True or user["number_of_free_message"] > 0:

                   
                     if user["active"]==False:
                      
                            t1 = CustomThread(target=get_chat, args=(user["pk"],text))     
                            t1.start() 
                            
                            new_number_of_free_message=user["number_of_free_message"]-1
                            User.objects.only('use','number_of_free_message').filter(pk=user['pk']).update(use=True,number_of_free_message=new_number_of_free_message)
                            this_advertisement="الاعلان"
                    
                    
                            current_time = datetime.datetime.now()
                            seconds = current_time.second
                            first_digit = str(seconds)[0]
                            advertisement_data=None

                            advertisement_check= advertisement.objects.values('pk','name','description').exclude(seen_advertisement__user__pk=user["pk"]).filter(country=user["country"],active_to_see=True,date_of_end__gte=datetime.datetime.now(timezone).date(),date_of_start__lte=datetime.datetime.now(timezone).date()).order_by('?').first()                   

                            if not advertisement_check is None:
                                   
                                   if first_digit in ['6','7','8','9']:
                    
                                     advertisement_data= advertisement.objects.values('pk','name','description').exclude(seen_advertisement__user__pk=user["pk"]).filter(country=user["country"],active_to_see=True,important_group=2,date_of_end__gte=datetime.datetime.now(timezone).date(),date_of_start__lte=datetime.datetime.now(timezone).date()).order_by('?').first()                          
                                   if first_digit in ['3','4','5']or advertisement_data is None:
                    
                                       advertisement_data= advertisement.objects.values('pk','name','description').exclude(seen_advertisement__user__pk=user["pk"]).filter(country=user["country"],active_to_see=True,important_group=1,date_of_end__gte=datetime.datetime.now(timezone).date(),date_of_start__lte=datetime.datetime.now(timezone).date()).order_by('?').first()
                          
                                   if first_digit in ['0','1','2'] or advertisement_data is None:
                                          advertisement_data=advertisement_check
                              
                            if advertisement_check is None:
                                   this_advertisement="لقد شاهدة الاعلان"
                                   if first_digit in ['6','7','8','9']:
                    
                                          advertisement_data= advertisement.objects.values('pk','name','description').filter(country=user["country"],active_to_see=True,important_group=2,date_of_end__gte=datetime.datetime.now(timezone).date(),date_of_start__lte=datetime.datetime.now(timezone).date()).order_by('?').first()                          
                                   if first_digit in ['3','4','5']or advertisement_data is None:
                    
                                          advertisement_data= advertisement.objects.values('pk','name','description').filter(country=user["country"],active_to_see=True,important_group=1,date_of_end__gte=datetime.datetime.now(timezone).date(),date_of_start__lte=datetime.datetime.now(timezone).date()).order_by('?').first()
                          
                                   if first_digit in ['0','1','2'] or advertisement_data is None:
                              
                                          advertisement_data= advertisement.objects.values('pk','name','description').filter(country=user["country"],active_to_see=True,date_of_end__gte=datetime.datetime.now(timezone).date(),date_of_start__lte=datetime.datetime.now(timezone).date()).order_by('?').first()                          
                                          

                            if advertisement_data is None:
                                   # system="answer"
                                   system= t1.join()
                                   chat.objects.create(user_chat=text,system_chat=system,user=User(pk=user["pk"]))
                                   send_message_T(chat_id,system)
                                   return Response(status=status.HTTP_200_OK)
                            else:
                                   encoded_phone =base64.b64encode(user['phone'].encode())
                                   # system="answer"

                                   system= t1.join()
                                   
                        
                                   chat.objects.create(user_chat=text,system_chat=system,user=User(pk=user["pk"]))
                                   url=reverse('redirectTO', kwargs={"pk":advertisement_data['pk'],"uuid":encoded_phone.decode('utf-8')},request=request)
                                   message=system+"\n \n"+this_advertisement+"\n \n"+advertisement_data['name']+"\n"+advertisement_data['description']+"\n"+url.replace(":8080",":80")
                                   send_message_T(chat_id,message)
                                   return Response(status=status.HTTP_200_OK)
  
  
                     else:
                            
                            chats=[]
                            all_chats=chat.objects.values('system_chat','user_chat').filter(user=user["pk"]).order_by('-pk')[:3]#########
                            for one_chat in all_chats:
                                   chats.append({"role":"user","content":one_chat['user_chat']})
                                   chats.append({"role":"assistant","content":one_chat['system_chat'].strip("\n").strip()})
                            chats.append({"role":"user","content":text})
                            response=openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=chats)
                            system=response['choices'][0]['message']['content'] 

                            # system="answer"                            
                            chat.objects.create(user_chat=text,system_chat=system,user=User(pk=user["pk"]))
                            send_message_T(chat_id,system)
                            return Response(status=status.HTTP_200_OK)
                            
                        
                        
                        
                        
                        
              message="لقد انتهت الرسائل المجانية"+"\n"+"للاشتراك يرجى زيارة موقعنا"+"https://web.telegram.org"
              send_message_T(chat_id,message)
              return Response(status=status.HTTP_200_OK)



