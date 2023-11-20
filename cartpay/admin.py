from django.contrib import admin
from .models import CartType,CartPrice,Pay
# Register your models here.
admin.site.register([CartType,CartPrice,Pay])