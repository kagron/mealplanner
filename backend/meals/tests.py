from django.test import TestCase
from .models import Meal
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

def create_meal(time_of_day, day, user):
    """
    Create a meal with the given `time_of_day`
    """
    created = timezone.now()
    updated = timezone.now()
    return Meal.objects.create(
        time_of_day=time_of_day,
        created=created, 
        updated=updated, 
        day=day,
        user=user
    )

def create_test_user(username, email):
    """
    Create a user with the given `username` and `email`
    """
    return User.objects.create_user(username, email)

# Create your tests here.
class MealModelTests(TestCase):
    def test_retrieve_only_breakfast_meals(self):
        """
        find only breakfast meals
        """
        day = datetime(2017, 1, 1)
        user = create_test_user(username="Kyle", email="test@example.com")
        create_meal(time_of_day=Meal.BREAKFAST, day=day, user=user)
        create_meal(time_of_day=Meal.LUNCH, day=day, user=user)
        meals = Meal.objects.filter(time_of_day=Meal.BREAKFAST)
        logger.info(meals)
        self.assertQuerysetEqual(
            meals,
            ['<Meal: Breakfast on January 01, 2017>']
        )