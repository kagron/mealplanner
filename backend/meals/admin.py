from django.contrib import admin

# Register your models here.
from .models import Meal, Food, Favorite

# admin.site.register(Meal)
class MealAdmin(admin.ModelAdmin):
    fields = ['id','user','day','time_of_day','created','updated',]
    readonly_fields=('id','created','updated',)

class FoodAdmin(admin.ModelAdmin):
    fields = ['id','meal','description','calories','created','updated',]
    readonly_fields=('id','created','updated',)

class FavoriteAdmin(admin.ModelAdmin):
    fields = ['id','food','user','created','updated',]
    readonly_fields=('id','created','updated',)

admin.site.register(Meal, MealAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Favorite, FavoriteAdmin)