from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.OneToOneField(to='CompanyAddress', on_delete=models.CASCADE, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    founded = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(to='Category', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class CompanyAddress(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        pass


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


