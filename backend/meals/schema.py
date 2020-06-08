from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id
from meals.models import Meal, Food, Favorite
from django.contrib.auth.models import User
from django.utils import timezone
import django_filters
import graphene

class TimesOfDayEnum(graphene.Enum):
    breakfast = Meal.BREAKFAST
    lunch     = Meal.LUNCH
    dinner    = Meal.DINNER

class MealNode(DjangoObjectType):
    class Meta:
        model = Meal

class AddMealMutation(graphene.Mutation):
    class Arguments:
        day         = graphene.Date()
        time_of_day = TimesOfDayEnum()
        user        = graphene.Int(required=True)

    meal = graphene.Field(MealNode)

    def mutate(self, info, day, time_of_day, user):
        userObj = User.objects.get(pk=user)
        meal    = Meal.objects.create(
            time_of_day = time_of_day,
            day         = day,
            created     = timezone.now(),
            updated     = timezone.now(),
            user        = userObj
        )
        return AddMealMutation(meal=meal)

class FoodNode(DjangoObjectType):
    class Meta:
        model = Food

class FavoriteNode(DjangoObjectType):
    class Meta:
        model = Favorite

class UserNode(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    all_meals     = graphene.List(MealNode)
    def resolve_all_meals(self, info, **kwargs):
        return Meal.objects.all()

    all_food      = graphene.List(FoodNode)

    all_favorites = graphene.List(FavoriteNode)

    all_users     = graphene.List(UserNode)

class Mutation(graphene.ObjectType):
    add_meal = AddMealMutation.Field()

    