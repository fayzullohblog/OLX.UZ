from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Ads,AdsAttributeValue,AdsAttributeValueOption,Category,SubCategory,AdsAttributeValueProxy
# Register your models here.
from django.contrib.admin import AdminSite
admin.site.register([Category,SubCategory])
from django.utils.html import mark_safe
from django.db.models import Count


# shu Mdollarni alohida chiqariadi ,

@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ("title",'get_price','image_preview','display_price_count','post_id','sub_category')
    readonly_fields = ('image_preview',)
    list_filter=("title",'price','post_id','sub_category')

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.image.url))
        else:
            return '(No image)'

    image_preview.short_description = 'Preview'



    def display_price_count(self, obj):
        return obj.price_count

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryset=super().get_queryset(request)
        queryset=queryset.annotate(
            price_count=Count('price')
        )
        return queryset
    
    def get_price(self,obj):
        return obj.price
    

    get_price.admin_order_field='price'        # ishlamadi tartiblash


@admin.register(AdsAttributeValue)
class AdsAttributeValueAdmin(admin.ModelAdmin):
    list_display=('value','ads','attribute')

class AdsAttributeValueProxyAdmin(admin.ModelAdmin):
    readonly_fields=('value','ads','attribute')

class AdsAdminSite(AdminSite):
    site_header = "UMSRA adss Admin"
    site_title = "UMSRA adss Admin Portal"
    index_title = "Welcome to UMSRA Researcher adss Portal"

ads_admin_site = AdsAdminSite(name='ads_admin')

@admin.register(AdsAttributeValueOption)
class AdsAttributeValueOptionAdmin(admin.ModelAdmin):
    list_display=('ads_attribute_value','option')


ads_admin_site.register(Ads)
ads_admin_site.register(Category)

