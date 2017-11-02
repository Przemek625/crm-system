from django.contrib import admin

# Register your models here.
from companies.models import Company, CustomerToCompany


@admin.register(Company)
class CompaniesAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomerToCompany)
class CustomerToCompanyAdmin(admin.ModelAdmin):
    pass
