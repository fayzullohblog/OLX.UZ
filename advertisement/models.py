from django.db import models
from utils.models import BaseModel
from users.models import User
from ads.models import Ads
# Create your models here.

class PriceAdvertisement(BaseModel):
    ads=models.ForeignKey(Ads,on_delete=models.PROTECT)
    view_couunt=models.IntegerField(default=0)
    price=models.IntegerField(default=0)


class Advertisement(BaseModel):
    title=models.CharField(max_length=100)
    price=models.ForeignKey(PriceAdvertisement,on_delete=models.SET_NULL,null=True)


class OtherAdvertisement(BaseModel):
    title=models.CharField(max_length=100)
    ads=models.ForeignKey(Ads,on_delete=models.PROTECT)
    view_couunt=models.IntegerField(default=0)
    state=models.BooleanField(default=False)
    


