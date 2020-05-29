from django.db import models
from django.contrib.auth.models import User
import django

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Meal(BaseModel):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    TIMES_OF_DAY = (
        (BREAKFAST, "Breakfast"),
        (LUNCH, "Lunch"),
        (DINNER, "Dinner")
    )
    time_of_day = models.CharField(choices=TIMES_OF_DAY, max_length=100)
    day = models.DateField(default=django.utils.timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return str(self.user.username + "'s " + self.get_time_of_day_display()) + " on " + self.day.strftime("%B %d, %Y")


class Food(BaseModel):
    meal = models.ForeignKey(Meal, related_name="food_in_meal", on_delete=models.CASCADE)
    description = models.TextField()
    calories = models.IntegerField()

    def __str__(self):
        return self.description + " with " + str(self.calories) + " calories"

class Favorite(BaseModel):
    food = models.ForeignKey(Food, related_name="favorited_food", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username + " favorited " + self.food.description


