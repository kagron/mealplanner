from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id
from meals.models import Meal, Food, Favorite
from django.contrib.auth.models import User
from django.utils import timezone
import django_filters
import graphene
from django.contrib.auth import authenticate, get_user_model
import graphql_jwt
from graphql_jwt.decorators import login_required

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

class RegisterMutation(graphene.Mutation):
    class Arguments:
        firstName = graphene.String(required=True)
        lastName = graphene.String(required=True)
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
    user = graphene.Field(UserNode)

    def mutate(self, info, firstName, lastName, username, email, password):
        user = User.objects.create_user(
            username,
            email,
            password
        )
        if not user:
            raise Exception('There was a problem creating your account. Please try again')
        user.first_name = firstName
        user.last_name = lastName
        user.save()

        return RegisterMutation(user=user)

class Query(graphene.ObjectType):
    user          = graphene.Field(UserNode)
    def resolve_user(self, info, **kwargs):
        if info.context.user.is_anonymous:
            return None
        return info.context.user;

    all_meals     = graphene.List(MealNode)
    def resolve_all_meals(self, info, **kwargs):
        return Meal.objects.all()

    all_food      = graphene.List(FoodNode)

    all_favorites = graphene.List(FavoriteNode)

    all_users     = graphene.List(UserNode)
    @login_required
    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

class Mutation(graphene.ObjectType):
    add_meal = AddMealMutation.Field()
    register = RegisterMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    