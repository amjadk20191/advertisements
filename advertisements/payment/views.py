
from rest_framework import views
from advertisements import settings
import requests
from core.models import User
import json
import datetime
from advertiser.models import advertisement
from rest_framework.response import Response
from rest_framework import status
from advertisements.settings import timezone

class PayPalWebhookView(views.APIView):
    def post(self, request):

        if "HTTP_PAYPAL_TRANSMISSION_ID" not in request.META:
             return Response(status=status.HTTP_400_BAD_REQUEST)
        url = 'https://api-m.sandbox.paypal.com/v1/oauth2/token'
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
        }


        auth = (settings.CLIENT_ID, settings.CLIENT_SECRET)

        response = requests.post(url, headers=headers, data=data, auth=auth)

        if not response.status_code == requests.codes.ok:
             return Response(status=status.HTTP_400_BAD_REQUEST)
        else:

            response_data = response.json()
            access_token = response_data['access_token']

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {access_token}",
            }
            data={
                "auth_algo":request.META['HTTP_PAYPAL_AUTH_ALGO'],
                "cert_url": request.META['HTTP_PAYPAL_CERT_URL'],
                "transmission_id": request.META['HTTP_PAYPAL_TRANSMISSION_ID'],
                "transmission_sig": request.META['HTTP_PAYPAL_TRANSMISSION_SIG'],
                "transmission_time": request.META['HTTP_PAYPAL_TRANSMISSION_TIME'],
                "webhook_id": settings.PAYPAL_WEBHOOK_ID ,
                "webhook_event": request.data }


            response = requests.post('https://api-m.sandbox.paypal.com/v1/notifications/verify-webhook-signature', headers=headers, data=json.dumps(data))

            if not response.status_code == requests.codes.ok:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
             data=request.data
             data_payment=data["resource"]["purchase_units"][0]["description"].split()
             if data_payment[-1]=="Baka":
                 User.objects.only('active',"dateOfEnd").filter(phone=data_payment[0]).update(dateOfEnd= datetime.datetime.now(timezone).date()+datetime.timedelta(days=int(data_payment[1])),active=True )
             if data_payment[-1]=="adv":
                 advertisement.objects.only('active_to_see').filter(pk=data_payment[0]).update(active_to_see=True )

                 
             













             return Response(status=status.HTTP_200_OK)



