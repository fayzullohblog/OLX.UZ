from django.contrib import admin
from .models import Language,Education,Experience,DriverLicence,Profile,JobForUser
# Register your models here.
admin.site.register([Language,Education,Experience,DriverLicence,Profile,JobForUser])







admin.site.site_header = "OLX User Admin"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to OLX Admin Panel"