from utils.models import BaseModel
from django.db import models
from users.models import User
from django.core.validators import RegexValidator
from common.models import District
# Create your models here.

class Language(BaseModel):
    title=models.CharField(max_length=30)

class Education(BaseModel):
    name=models.CharField(max_length=30)
    specially=models.CharField(max_length=50)

    start_date=models.DateTimeField()
    finished_date=models.DateTimeField()

    new_field=models.IntegerField(default=0)
    precentage=models.IntegerField(default=25)

    work_state=models.BooleanField(default=False)

    
class Experience(BaseModel):
    position_name=models.CharField(max_length=30)
    employer=models.CharField(max_length=50)
    about_work=models.TextField()

    start_date=models.DateTimeField()
    finished_date=models.DateTimeField()

    precentage=models.IntegerField(default=40)           
    new_field=models.IntegerField(default=0)
    
    work_state=models.BooleanField(default=False)

class DriverLevelChoice(models.TextChoices):
        none=None
        A='A'
        B='B'
        C='C'
        D='D'
        BE='B+E'
        CE='C+E'
        DE='D+E'




class DriverLicence(BaseModel):
    level_choice=models.CharField(max_length=4,default=DriverLevelChoice.none,choices=DriverLevelChoice.choices)
    percentage=models.IntegerField(default=5)
    state=models.BooleanField(default=False)

                    

class Profile(BaseModel):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    password=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=RegexValidator(
            regex=r'^9989[0-9]{9}',
            message="Telefon raqamingiz 9 bilan boshlanishi va 12 ta belgidan iborat bo'lishi kerak. Masalan: 998901235476",
                                )
    resume=models.FileField()
    
    language=models.ManyToManyField(Language)
    education=models.ForeignKey(Education,on_delete=models.SET_NULL,null=True,blank=True)
    experience=models.OneToOneField(Experience,on_delete=models.CASCADE,null=True,blank=True)
    driver_licence=models.OneToOneField(DriverLicence,on_delete=models.SET_NULL,null=True,blank=True)

    other_experience=models.CharField(max_length=300,null=True,blank=True)
    hobby=models.TextField()



class SalaryTypeChoice(models.TextChoices):
        sum='SUM'
        euro='EURO'
       

class PerDay_Or_PerMonthChoice(models.TextChoices):
        day='day'
        month='month'

class TimeJobChoice(models.TextChoices):
        fully='Tuliq stavkada bandlik'
        no_fully='Tuliq bolmagan bandlik'

class TypeJobChoice(models.TextChoices):
        always_busy='Doimiy bandlik'
        temporary_busy='Vaqtinchalik bandlik'

class JobForUser(BaseModel):
     
     user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
     distirct=models.ForeignKey(District,on_delete=models.CASCADE)

     type_work=models.CharField(max_length=50)
     time_job=models.CharField(max_length=30,default=TimeJobChoice.fully,choices=TimeJobChoice.choices)
     type_job=models.CharField(max_length=30,default=TypeJobChoice.always_busy,choices=TypeJobChoice.choices)
     salary_type=models.CharField(max_length=4,default=SalaryTypeChoice.sum,choices=SalaryTypeChoice.choices)
     day_or_month=models.CharField(max_length=6,default=PerDay_Or_PerMonthChoice.day,choices=PerDay_Or_PerMonthChoice.choices)

     least_price=models.IntegerField(default=0)








    