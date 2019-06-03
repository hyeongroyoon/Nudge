from django.conf.urls import url, include
from myapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'today', views.Today_recipes)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^recipes', views.Recommend_recipes.as_view()),
    url(r'^choice-menu', views.Choice_recipe.as_view()),
]