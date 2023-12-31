from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model
from users.models import User
from django.utils.html import mark_safe
# Create your models here.
User = get_user_model()


class Category(BaseModel):
    # user=models.ForeignKey(User,on_delete=models.PROTECT)

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="main_category")

    ads_count = models.IntegerField(default=0)


    
class SubCategory(BaseModel):
    title = models.CharField(max_length=255)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategory"
    )
    attributes = models.ManyToManyField("attribute.Attribute", blank=True)

    ads_count = models.IntegerField(default=0)


class Ads(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="ads_images")
    price = models.IntegerField(default=0)
    content = models.TextField()

    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="sub_category"
    )
    district = models.ForeignKey("common.District", on_delete=models.CASCADE)

    is_top = models.BooleanField(default=False)
    
    post_id=models.CharField(max_length=20)

    from_finished_time=models.DateTimeField()
    to_finished_time=models.DateTimeField()

    address = models.CharField(max_length=255, null=True, blank=True)

    def get_address_text(self):
        return f"{self.district.region.title}, {self.district.title}"
    
    # def price_count(self):
    #      return self.price.count()

class AdsProxy(Ads):

    class Meta:
        proxy = True



class AdsAttributeValue(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)

    ads = models.ForeignKey(
        Ads, on_delete=models.CASCADE, related_name="attribute_values"
    )
    attribute = models.ForeignKey("attribute.Attribute", on_delete=models.CASCADE)

    

class AdsAttributeValueProxy(Ads):
    
    class Meta:
        
        proxy = True
class AdsAttributeValueOption(BaseModel):
    ads_attribute_value = models.ForeignKey(
        AdsAttributeValue, on_delete=models.CASCADE, related_name="value_options"
    )
    option = models.ForeignKey("attribute.AttributeOption", on_delete=models.CASCADE)


    # class Meta:
    #     db_name='ads_attribute_value_option_show'