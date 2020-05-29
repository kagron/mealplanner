from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import ObjectType, String, Mutation, Enum, DateTime, Int, relay, Field, resolve_only_args
from graphql_relay import from_global_id
from meals.models import Meal, Food, Favorite
from django.contrib.auth.models import User
from django.utils import timezone
import django_filters

class MealNode(DjangoObjectType):
    class Meta:
        model = Meal
        interfaces = (relay.Node,)
        filter_fields = ['time_of_day', 'day']

    @classmethod
    def get_node(cls, info, id):
        return Meal.objects.get(pk=id)

class AddMealMutation(relay.ClientIDMutation):
    class Input:
        day = DateTime()
        user = Int()
        # time_of_day = Enum.from_enum(enum=Meal.TIMES_OF_DAY)
    
    meal = Field(MealNode)

    @classmethod
    def mutate_and_get_payload(
        self,
        root,
        info,
        day,
        user,
        client_mutation_id=None
    ):
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
        interfaces = (relay.Node,)
        filter_fields = ["meal"]
    
    # @classmethod
    # def get_node(cls, info, id):
    #     print("HELLLOOOOOO")
    #     return Food.objects.get(pk=id)


class AddFoodMutation(relay.ClientIDMutation):
    class Input:
        meal = Int()
        description = String()
        calories = Int()
    
    food = Field(FoodNode)

    @classmethod
    def mutate_and_get_payload(
        self,
        root,
        info,
        meal,
        description,
        calories,
        client_mutation_id=None
    ):
        created = timezone.now()
        updated = timezone.now()
        new_food = Food.objects.create(
            meal=meal,
            created=created, 
            updated=updated, 
            description=description,
            calories=calories
        )
        return AddFoodMutation(food=new_food)

class FavoriteNode(DjangoObjectType):
    class Meta:
        model = Favorite
        interfaces = (relay.Node,)
        filter_fields = ["user"]
            
    @classmethod
    def get_node(cls, info, id):
        return Favorite.objects.get(pk=id)

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)
        filter_fields = ["username"]
         
    @classmethod
    def get_node(cls, info, user_id):
        print("HELLLOOOOOO")
        print(user_id)
        return User.objects.get(id=user_id)

class Query(ObjectType):
    node = relay.Node.Field()
    meal = relay.Node.Field(MealNode, meal_id=Int())
    all_meals = DjangoFilterConnectionField(MealNode)

    food = relay.Node.Field(FoodNode, food_id=Int())
    all_food = DjangoFilterConnectionField(FoodNode)

    favorites = relay.Node.Field(FavoriteNode)
    all_favorites = DjangoFilterConnectionField(FavoriteNode)

    users = relay.Node.Field(UserNode)
    user = relay.Node.Field(UserNode, user_id=Int())
    all_users = DjangoFilterConnectionField(UserNode)

    @resolve_only_args
    def resolve_user(self, user_id):
        return User.objects.get(id=user_id)

class Mutation(ObjectType):
    add_meal = AddMealMutation.Field()
    add_food_to_meal = AddFoodMutation.Field()
    