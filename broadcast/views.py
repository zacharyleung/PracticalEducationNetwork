from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import TwilioRestClient
from pen.local_settings import AC_SSID, AUTH_TOCKEN, FROM_NUMBER
from pen.global_settings import ADMIN_NUMBER
from models import Teacher, Message
from forms import MessageForm

# Create your views here.


def send_message(number, message_string):
    account_sid = AC_SSID
    auth_token = AUTH_TOCKEN
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(
        body = message_string,
        to = number,
        from_ = FROM_NUMBER)
    print message.sid


# broadcast a message from a teacher to everyone
def broadcast_message_teacher(sender_teacher, message_string):
    # log the message in the database
    new_message = Message(sender = sender_teacher,
        message = message_string)
    new_message.save()

    teachers = Teacher.objects.all()
    # exclude the admin teacher
    teachers = Teacher.objects.filter().exclude(number = ADMIN_NUMBER)
    for teacher in teachers:
        send_message(teacher.number, message_string)
    


def broadcast_message(request):
    if request.method== "GET":
        form = MessageForm()
        return render(request, 'broadcast.html', {
                            'form': form,
                        })

    elif request.method== "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message_string = form.cleaned_data['message']
            # send a message as the admin teacher
            admin_teacher, created = Teacher.objects.get_or_create(
                name = "Admin", number = ADMIN_NUMBER) 
            broadcast_message_teacher(admin_teacher, message_string)

        return HttpResponse("Sent successfully!")
