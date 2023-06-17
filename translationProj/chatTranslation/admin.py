from django.contrib import admin
from .models import User, Message
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('unique_id','lname', 'fname', 'mail', 'password', 'language', 'img', 'status')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('incoming_msg_id', 'outgoing_msg_id','msg', 'translated_msg')