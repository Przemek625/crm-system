from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django.contrib.auth import get_user_model
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
