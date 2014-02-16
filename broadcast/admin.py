from django.contrib import admin
from models import Teacher, Message

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')
admin.site.register(Teacher, TeacherAdmin)

class MessageAdmin(admin.ModelAdmin):
    pass
    #list_display = ('name', 'number')
admin.site.register(Message, MessageAdmin)
