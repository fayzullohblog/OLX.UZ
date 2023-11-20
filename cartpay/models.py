from django.db import models
from utils.models import BaseModel
from users.models import User
# Create your models here.

class CartType(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='image/cart_type')
    current_price=models.OneToOneField('CartPrice',on_delete=models.PROTECT,primary_key=True)

class CartPrice(BaseModel):
    count_price=models.IntegerField(default=0)
    state=models.BooleanField(default=False)


class Pay(BaseModel):
    carttype=models.ForeignKey(CartType,on_delete=models.SET_NULL,null=True)
    price=models.IntegerField(default=0)
    id_number=models.CharField(max_length=15)


    
