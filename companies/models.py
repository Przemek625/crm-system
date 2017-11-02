from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


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
    added_by = models.ForeignKey(to=User, null=True, blank=True)
    # last_edited = models.DateField(auto_now=True)
    customers = models.ManyToManyField(to=User, through='CustomerToCompany', related_name='customers')

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class CustomerToCompany(models.Model):
    """This models represents relations between company and its customers."""

    NOT_SPECIFIED = 'NS'
    WELL_INFORMED = 'WI'
    ANNOYED_ONE = 'AO'
    SUSPICIOUS_ONE = 'S'
    QUESTIONER = 'Q'
    ONES_WHO_AGREE_ON_EVERYTHING = 'OWAOE'
    INDECISIVE = 'I'

    CUSTOMER_TYPE_CHOICES = (
        (NOT_SPECIFIED, 'Not Specified'),
        (WELL_INFORMED, 'Well-Informed'),
        (ANNOYED_ONE, 'Annoyed One'),
        (SUSPICIOUS_ONE, 'Suspicious One'),
        (QUESTIONER, 'Questioner'),
        (ONES_WHO_AGREE_ON_EVERYTHING, 'Ones Who Agree On Everything'),
        (INDECISIVE, 'Indecisive'),

    )

    customer_type = models.CharField(
        max_length=5,
        choices=CUSTOMER_TYPE_CHOICES,
        default=NOT_SPECIFIED,
    )

    customer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    company = models.ForeignKey(to='Company', on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "{} to {}".format(self.customer, self.company)


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
