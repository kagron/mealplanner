from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Meal(models.Model):
    BREAKFAST = 0
    LUNCH = 1
    DINNER = 2
    TIMES_OF_DAY = (
        (BREAKFAST, "Breakfast"),
        (LUNCH, "Lunch"),
        (DINNER, "Dinner")
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    time_of_day = models.IntegerField(choices=TIMES_OF_DAY)
    day = models.DateField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.get_time_of_day_display() + " on " + self.day.strftime("%B %d, %Y")


class Food(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    description = models.TextField()
    calories = models.IntegerField()

