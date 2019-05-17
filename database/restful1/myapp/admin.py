from django.contrib import admin
from .models import *

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ('menu_name','how_make','sort','calorie','carbohydrate','protein', 'fat', 'salt','big_image', 'small_image', 'count')

admin.site.register(Menu)
admin.site.register(Market)
admin.site.register(MenuRecipe)
admin.site.register(Recipe)
admin.site.register(TakePicIngredients)
admin.site.register(Users)
admin.site.register(Ingredients)

