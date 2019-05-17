from myapp.models import MyappFood
from rest_framework import serializers

# 사용자의 재료에 따라 첫 번째로 추천 레시피들을 전달할 때 쓰는 serializer
class firstSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyappFood
        fields = ('id', 'recipe_name')

# 사용자가 최종 선택한 레시피의 모든 정보를 전달 할 때 쓰는 serializer
class secondSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyappFood
        fields = ('recipe_name', 'ingredients', 'direction')