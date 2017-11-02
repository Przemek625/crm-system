from django import forms

from companies.models import CustomerToCompany, Company


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class CustomerToCompanyForm(forms.ModelForm):
    class Meta:
        model = CustomerToCompany
        exclude = ('customer', )

    def __init__(self, *args, **kwargs):
        """
        We override this method to limit companies list showed in a form to these added user that
        makes the request.
        """
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.filter(added_by=user)


class CustomerToCompanyDeleteForm(forms.ModelForm):
    class Meta:
        model = CustomerToCompany
        fields = ('company', )

    def __init__(self, *args, **kwargs):
        """
        We override this method to limit companies list showed in a form to these added user that
        makes the request.
        """
        customer_id = kwargs.pop('customer_id')
        super().__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects\
            .filter(customertocompany__customer_id=customer_id)
