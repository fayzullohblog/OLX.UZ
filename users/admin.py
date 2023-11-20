from django.contrib import admin
from .models import User,OTP,Comment

admin.site.register([User,OTP,Comment])