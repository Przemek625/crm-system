from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DetailView

from companies.forms import CompanyForm
from companies.models import Company


class CompaniesListView(ListView):
    """This view list companies."""
    template_name = 'companies.html'
    model = Company
    context_object_name = 'company_list'
    paginate_by = 10


class CompanyDetailView(DetailView):
    """This view returns details of a company."""
    template_name = 'company_detail.html'
    context_object_name = 'company'
    model = Company

    def get_context_data(self, **kwargs):
        # TODO add Company address to context.
        context = super().get_context_data(**kwargs)
        context['test'] = 'test'
        return context


# TODO implement who added the company
class CompanyCreateView(CreateView):
    """This view is responsible for adding companies."""
    model = Company
    template_name = 'add_or_update_company.html'
    form_class = CompanyForm
    success_url = reverse_lazy('companies')

    def form_valid(self, form):
        """We override this method to determine currently log in user as the person that added the company."""
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class CompanyUpdateView(UpdateView):
    """This view is responsible for updating companies."""
    model = Company
    template_name = 'add_or_update_company.html'
    exclude = ('date_added', )
    success_url = reverse_lazy('companies')


class CompanyDeleteView(View):
    """This view is responsible for deleting companies."""
    model = Company
    redirect_view_name = 'companies'

    # TODO check if the object belongs to the user that makes the request.
    def post(self, request, pk):
        company = get_object_or_404(self.model, pk=pk)
        company.delete()
        return redirect(self.redirect_view_name)


class JoinCompanyView(View):
    """This view allows the user to join to a company."""
    def post(self, request):
        pass
