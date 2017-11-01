from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.views.generic import ListView
from django.contrib.auth import get_user_model

from companies.models import CustomerToCompany
from users.forms import LoginForm


class LoginView(View):
    """This view is responsible for login users."""
    login_form = LoginForm
    login_template = 'login.html'

    def get(self, request):
        return render(request, self.login_template, {'form': self.login_form()})

    def post(self, request):
        form = self.login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('companies')
            else:
                return render(request, self.login_template, {'message': 'Invalid username or password.'})
        else:
            return render(request, self.login_template, {'form': self.login_form()})


class RegistrationView(View):
    """This view is responsible for user registration."""
    registration_form = UserCreationForm
    registration_template = 'registration.html'

    def get(self, request):
        return render(request, self.registration_template, {'form': self.registration_form()})

    def post(self, request):
        form = self.registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration')
        else:
            return render(request, self.registration_template, {'form': form})


class UserListViews(ListView):
    """This view is responsible for listing users."""
    template_name = 'users.html'
    model = get_user_model()
    context_object_name = 'user_list'
    paginate_by = 10


# TODO user can only add customer to companies that he created.
class AddUserToCustomersView(LoginRequiredMixin, CreateView):
    """This view adds the user to company customers."""
    template_name = 'add_customer.html'
    model = CustomerToCompany
    success_url = reverse_lazy('users')

    def get_form_kwargs(self):
        """"We override this method..."""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class RemoveUserFromCustomersView(LoginRequiredMixin, View):
    """This view removes the user from company customers."""
    model = CustomerToCompany
    redirect_view_name = 'users'

    def post(self, request, customer_id):
        customer_to_company = get_object_or_404(self.model, customer_id=customer_id)
        if customer_to_company.company.added_by == request.user:
            customer_to_company.delete()
            return redirect(self.redirect_view_name)
        return HttpResponseForbidden()
