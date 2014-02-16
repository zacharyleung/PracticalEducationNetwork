from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import TwilioRestClient
from pen.local_settings import AC_SSID, AUTH_TOCKEN, FROM_NUMBER
from models  import Teacher
from forms import MessageForm

# Create your views here.


def msg_send(number, msg):
    account_sid = AC_SSID
    auth_token = AUTH_TOCKEN
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body=msg,
    to= number,
    from_=FROM_NUMBER)
    print message.sid

def broadcast_message(request):
    if request.method== "GET":
        form = MessageForm()
        return render(request, 'broadcast.html', {
                            'form': form,
                        })

    elif request.method== "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            teachers = Teacher.objects.all()
            for teacher in teachers:
                msg_send(teacher.number , form.cleaned_data['message'])

        return HttpResponse("Sent successfully!")
