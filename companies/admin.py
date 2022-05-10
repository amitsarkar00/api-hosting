from django.contrib import admin
from .models import Company, Hr, Admin

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Hr)
class HrAdmin(admin.ModelAdmin):
    pass

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    pass