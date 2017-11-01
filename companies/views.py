from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DetailView

from companies.forms import CompanyForm
from companies.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin


class CompaniesListView(LoginRequiredMixin, ListView):
    """This view list companies."""
    template_name = 'companies.html'
    model = Company
    context_object_name = 'company_list'
    paginate_by = 10


class CompanyDetailView(LoginRequiredMixin, DetailView):
    """This view returns details of a company."""
    template_name = 'company_detail.html'
    context_object_name = 'company'
    model = Company

    def get_context_data(self, **kwargs):
        # TODO add some feature like display
        context = super().get_context_data(**kwargs)
        context['test'] = 'test'
        return context


class CompanyCreateView(LoginRequiredMixin, CreateView):
    """This view is responsible for adding companies."""
    model = Company
    template_name = 'add_or_update_company.html'
    form_class = CompanyForm
    success_url = reverse_lazy('companies')

    def form_valid(self, form):
        """We override this method to determine currently log in user as the person that added the company."""
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    """This view is responsible for updating companies."""
    model = Company
    template_name = 'add_or_update_company.html'
    exclude = ('date_added', )
    success_url = reverse_lazy('companies')


class CompanyDeleteView(LoginRequiredMixin, View):
    """This view is responsible for deleting companies."""
    model = Company
    redirect_view_name = 'companies'

    def post(self, request, pk):
        company = get_object_or_404(self.model, pk=pk)
        # Check if the company is added by the user that makes the request.
        if company.added_by == request.user:
            company.delete()
            return redirect(self.redirect_view_name)
        return HttpResponseForbidden()
