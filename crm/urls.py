"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from companies.views import CompaniesListView, CompanyDetailView, CompanyDeleteView, CompanyCreateView,\
    CompanyUpdateView
from users.views import LoginView, RegistrationView, AddUserToCustomersView, UserListViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    url(r'^companies/$', CompaniesListView.as_view(), name='companies'),
    url(r'^companies/(?P<pk>\d+)$', CompanyDetailView.as_view(), name='company-detail'),
    url(r'^delete-company/(?P<pk>\d+)$', CompanyDeleteView.as_view(), name='delete-company'),
    url(r'^add-company/$', CompanyCreateView.as_view(), name='add-company'),
    url(r'^update-company/(?P<pk>\d+)$', CompanyUpdateView.as_view(), name='update-company'),
    url(r'^logout/$', LogoutView.as_view(next_page='login'), name='logout'),
    url(r'^logout/$', LogoutView.as_view(next_page='login'), name='logout'),
    url(r'^add-user-to-customers/$', AddUserToCustomersView.as_view(), name='add_user_to_customers'),
    url(r'^users/$', UserListViews.as_view(), name='users')
]
