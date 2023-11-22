from django.contrib import admin
from .models import User,OTP,Comment
from django.contrib.auth.models import Group


admin.site.register([User,OTP,Comment])
admin.site.unregister([Group,OTP])

