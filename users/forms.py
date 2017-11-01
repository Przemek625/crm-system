from django import forms

from companies.models import CustomerToCompany, Company


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class CustomerToCompanyForm(forms.Form):
    """"""

    def __init__(self, user, *args, **kwargs):
        """We override this method to..."""
        super().__init__(*args, **kwargs)
        # self.company = forms.ChoiceField(queryset=Company.objects.filter(added_by=user))
        self.fields['company'].queryset = Company.objects.filter(added_by=user)

    class Meta:
        model = CustomerToCompany
