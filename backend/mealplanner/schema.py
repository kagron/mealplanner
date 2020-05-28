import meals.schema
import graphene

from graphene_django.debug import DjangoDebug

class Query(
    meals.schema.Query,
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name="_debug")

class Mutation(
    meals.schema.Mutation,
    graphene.ObjectType
):
    debug: graphene.Field(DjangoDebug, name="__debug")

schema = graphene.Schema(query=Query, mutation=Mutation)
