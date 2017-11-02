from django import forms

from companies.models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        exclude = ['date_added', 'added_by', 'customers']
