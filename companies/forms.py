from django.forms import ModelForm

from companies.models import Company


class CompanyForm(ModelForm):

    class Meta:
        model = Company
        exclude = ['date_added', 'added_by', 'customers']
