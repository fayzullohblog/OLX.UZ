from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from utils.models import BaseModel


class User(AbstractUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    password=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    # _phone_number=RegexValidator(
    #         regex=r'^9989[0-9]{9}',
    #         message="Telefon raqamingiz 9 bilan boshlanishi va 12 ta belgidan iborat bo'lishi kerak. Masalan: 998901235476",
    #                             )
    # phone_number=models.CharField(
    #     max_length=20,
    #     validators=[_phone_number],
    #     unique=True
    # )

    facecook=models.URLField(max_length=250)
    google=models.URLField(max_length=250)
    apple=models.URLField(max_length=250)

    state=models.BooleanField(default=False)

    USERNAME_FIELD="username"
    REQUIRED_FIELDS=['email']






class OTP(BaseModel):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    code=models.CharField(max_length=6)
    created_at=models.DateTimeField()
    activate_till=models.DateTimeField()
    activatted=models.DateTimeField()



class Comment(BaseModel):
    from ads.models import Ads
    post = models.ForeignKey(Ads, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    author = models.CharField(max_length=200)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    class Meta:
        ordering = ['created_at']




