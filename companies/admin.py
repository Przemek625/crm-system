from django.contrib import admin

# Register your models here.
from companies.models import Company, CustomerToCompany, Category


@admin.register(Company)
class CompaniesAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomerToCompany)
class CustomerToCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
