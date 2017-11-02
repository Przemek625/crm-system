from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from companies.views import CompaniesListView, CompanyDetailView, CompanyDeleteView, CompanyCreateView,\
    CompanyUpdateView
from users.views import LoginView, RegistrationView, AddUserToCustomersView, UserListViews, RemoveUserFromCustomersView

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
    url(r'^add-user-to-customers/(?P<pk>\d+)$', AddUserToCustomersView.as_view(), name='add_user_to_customers'),
    url(r'^users/$', UserListViews.as_view(), name='users'),
    url(r'^delete-user-from-customers/(?P<pk>\d+)$', RemoveUserFromCustomersView.as_view(),
        name='delete-user-from-customers'),

]
