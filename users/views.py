from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.views.generic import ListView

from companies.models import CustomerToCompany
from users.forms import LoginForm, CustomerToCompanyForm, CustomerToCompanyDeleteForm
from django.contrib.auth import get_user_model

User = get_user_model()


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
                return render(request, self.login_template, {
                    'message': 'Invalid username or password.',
                    'form': self.login_form()
                })
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
            return redirect('login')
        else:
            return render(request, self.registration_template, {'form': form})


class UserListViews(LoginRequiredMixin, ListView):
    """This view is responsible for listing users."""
    template_name = 'users.html'
    model = get_user_model()
    context_object_name = 'user_list'
    paginate_by = 10


class AddUserToCustomersView(LoginRequiredMixin, CreateView):
    """
    This view adds the user to company customers. Note that the user that makes the request can
    only choose companies added by himself.
    """
    template_name = 'add_customer.html'
    model = CustomerToCompany
    success_url = reverse_lazy('users')
    form_class = CustomerToCompanyForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user_id = self.kwargs['pk']
        form.instance.customer = User.objects.get(id=user_id)
        return super().form_valid(form)


class RemoveUserFromCustomersView(LoginRequiredMixin, View):
    """This view removes the user from company's customers."""
    model = CustomerToCompany
    redirect_view_name = 'users'
    template_name = 'remove_user_from_customers.html'

    def post(self, request, customer_id):
        customer = User.objects.get(id=customer_id)
        form = CustomerToCompanyDeleteForm(request.POST)
        if form.is_valid():
            CustomerToCompany.objects.get(company=form['company'], customer=customer).delete()
            return redirect(self.redirect_view_name)
        else:
            return render(request, self.template_name, {'form': form, 'customer': customer})

    def get(self, request, customer_id):
        customer = User.objects.get(id=customer_id)
        form = CustomerToCompanyDeleteForm(customer_id=customer_id)
        return render(request, self.template_name, {'form': form, 'customer': customer})
