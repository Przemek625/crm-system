from django.db import models
from django.contrib.auth import get_user_model


class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    founded = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(to='Category', null=True, blank=True)
    city = models.CharField(max_length=255, )
    region = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    date_added = models.DateField(auto_now=True)
    added_by = models.ForeignKey(to=get_user_model(), null=True, blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


