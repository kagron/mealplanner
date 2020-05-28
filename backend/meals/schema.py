from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import Node, ObjectType, String, Mutation, Enum, DateTime, Int, relay
from graphql_relay import from_global_id
from meals.models import Meal, Food, Favorite
from django.contrib.auth.models import User
from django.utils import timezone
import django_filters

class MealNode(DjangoObjectType):
    class Meta:
        model = Meal
        interfaces = (Node,)
        filter_fields = ['time_of_day', 'day']

class AddMealMutation(Mutation):
    class Arguments:
        day = DateTime()
        user = Int()
        # time_of_day = Enum.from_enum(enum=Meal.TIMES_OF_DAY)
    
    meal = Node.Field(MealNode)

    def mutate(self, info, day, user):
        created = timezone.now()
        updated = timezone.now()
        userObj = User.objects.get(pk=user)
        new_meal = Meal.objects.create(
            time_of_day="lunch",
            created=created, 
            updated=updated, 
            day=day,
            user=userObj
        )
        return AddMealMutation(meal=new_meal)

class FoodNode(DjangoObjectType):
    class Meta:
        model = Food
        interfaces = (Node,)
        filter_fields = ["meal"]

class FavoriteNode(DjangoObjectType):
    class Meta:
        model = Favorite
        interfaces = (Node,)
        filter_fields = ["user"]

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (Node,)
        filter_fields = ["username"]

class Query(ObjectType):
    meal = Node.Field(MealNode)
    all_meals = DjangoFilterConnectionField(MealNode)

    food = Node.Field(FoodNode)
    all_food = DjangoFilterConnectionField(FoodNode)

    favorites = Node.Field(FavoriteNode)
    all_favorites = DjangoFilterConnectionField(FavoriteNode)

    users = Node.Field(UserNode)
    user = Node.Field(UserNode, user_id=String())
    all_users = DjangoFilterConnectionField(UserNode)

class Mutation(ObjectType):
    add_meal = AddMealMutation.Field()
    