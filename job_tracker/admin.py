from django.contrib import admin
from .models import Company, HiringManager, Job
# Register your models here.

admin.site.register(Company)
admin.site.register(HiringManager)
admin.site.register(Job)
