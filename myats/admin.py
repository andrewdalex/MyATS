from django.contrib import admin
from .models import *




admin.site.register(Student)
admin.site.register(Resource)
admin.AdminSite.site_header = 'ATS Administration'
admin.AdminSite.site_title = 'ATS Administration'
admin.AdminSite.site_url = '/search/'
admin.AdminSite.index_title = 'ATS Administration'
