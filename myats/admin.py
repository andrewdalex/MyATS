from django.contrib import admin
from .models import *

class ReceivedFormInline(admin.TabularInline):
    model = ReceivedForm
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    inlines = (ReceivedFormInline,)

admin.site.register(Student, StudentAdmin)
admin.site.register(Class)
admin.site.register(Resource)
admin.site.register(Form)
admin.AdminSite.site_header = 'ATS Administration'
admin.AdminSite.site_title = 'ATS Administration'
admin.AdminSite.site_url = '/home/'
admin.AdminSite.index_title = 'ATS Administration'
