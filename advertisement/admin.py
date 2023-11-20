from django.contrib import admin
from .models import PriceAdvertisement,OtherAdvertisement,Advertisement
# Register your models here.
admin.site.register([PriceAdvertisement,OtherAdvertisement,Advertisement])
