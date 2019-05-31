from django.conf.urls import url
from myapp import views

urlpatterns = [
    url(r'^recipes', views.Recommend_recipes.as_view()),
    url(r'^choice-menu', views.Final_recipe.as_view()),
]