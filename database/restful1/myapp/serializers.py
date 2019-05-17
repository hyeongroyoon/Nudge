from myapp.models import *
from rest_framework import serializers

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('menu_name','how_make','sort','calorie','carbohydrate','protein', 'fat', 'salt','big_image', 'small_image', 'count')
