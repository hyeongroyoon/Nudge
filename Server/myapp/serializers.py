from myapp.models import Menu
from rest_framework import serializers

# 사용자의 재료에 따라 첫 번째로 추천 레시피들을 전달할 때 쓰는 serializer
class Recommend(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('mname', 'dimage')

# 사용자가 최종 선택한 레시피의 모든 정보를 전달 할 때 쓰는 serializer
class Final(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('mname', 'ingredient')