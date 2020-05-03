from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import Node, ObjectType
from meals.models import Meal, Food
import django_filters

class MealNode(DjangoObjectType):
    class Meta:
        model = Meal
        interfaces = (Node,)
        filter_fields = ['time_of_day', 'day']

class FoodNode(DjangoObjectType):
    class Meta:
        model = Food
        interfaces = (Node,)
        filter_fields = ["meal"]

class Query(ObjectType):
    meal = Node.Field(MealNode)
    all_meals = DjangoFilterConnectionField(MealNode)

    food = Node.Field(FoodNode)
    all_food = DjangoFilterConnectionField(FoodNode)
    