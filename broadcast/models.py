from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=250)
    number = models.CharField(max_length=20)

class Message(models.Model):
    sender = models.ForeignKey('Teacher')
    message = models.CharField(max_length=160)
