from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import TwilioRestClient
from pen.local_settings import AC_SSID, AUTH_TOCKEN
from models  import Teacher
# Create your views here.


def send_messages(request):
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = AC_SSID
    auth_token = AUTH_TOCKEN
    client = TwilioRestClient(account_sid, auth_token)

    teachers = Teacher.objects.all()

    for teacher in teachers:
        message = client.messages.create(body="Hallo world of PEN. Hahahaha",
        to= teacher.number,
        from_="+14844890949")
        print message.sid

    return HttpResponse("Sent successfully!")
