from django.contrib import admin
from .models import Ads,AdsAttributeValue,AdsAttributeValueOption,Category,SubCategory
# Register your models here.
admin.site.register([Ads,AdsAttributeValue,AdsAttributeValueOption,Category,SubCategory])