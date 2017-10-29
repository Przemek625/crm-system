from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth import login, authenticate
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
            # TODO handle fail of authentication
            user = authenticate(username=username, password=password)
            login(request, user)
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
            return render(request, LoginView.login_template, {'register_success': True})
        else:
            return render(request, self.registration_template, {'form': form})


