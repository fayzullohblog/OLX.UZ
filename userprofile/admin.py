from django.contrib import admin
from .models import Language,Education,Experience,DriverLicence,Profile,JobForUser
# Register your models here.
admin.site.register([Language,Education,Experience,DriverLicence,Profile,JobForUser])