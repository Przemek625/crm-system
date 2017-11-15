import graphene

from graphene_django.types import DjangoObjectType

from companies.models import Company, CustomerToCompany


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company


class CustomerToCompanyType(DjangoObjectType):
    class Meta:
        model = CustomerToCompany


class Query(graphene.AbstractType):
    company = graphene.Field(
        CompanyType,
        id=graphene.Int(),
        name=graphene.String()
    )
    all_companies = graphene.List(CompanyType)
    all_customers = graphene.List(CustomerToCompanyType)

    def resolve_all_companies(self, info, **kwargs):
        return Company.objects.all()

    def resolve_all_customers(self, info, **kwargs):
        return CustomerToCompany().objects.select_related('customers').all()

    def resolve_company(self, info, **kwargs):
        company_id = kwargs.get('id')
        company_name = kwargs.get('name')

        if company_id:
            return Company.objects.get(pk=company_id)

        if company_name:
            return Company.objects.get(name=company_name)

        return None
