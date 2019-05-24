from django.conf.urls import url, include
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()

router.register(r'recipes', views.Recommend_recipes)
router.register(r'final-recipe', views.Final_recipe)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]



