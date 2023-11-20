from django.contrib import admin
from .models import Attribute,AttributeOption


# Register your models here.
admin.site.register([AttributeOption,Attribute])