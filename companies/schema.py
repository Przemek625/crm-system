import companies.graphne.schema

import graphene


class Query(companies.graphne.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
