from django.contrib import admin
from .models import *
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(SummerClass)
admin.site.register(Enrollment)
admin.site.register(Resource)
admin.AdminSite.site_header = 'ATS Administration'
admin.AdminSite.site_title = 'ATS Administration'
admin.AdminSite.site_url = '/home/'
admin.AdminSite.index_title = 'ATS Administration'
