from django.conf.urls import url
from myapp import views

urlpatterns = [
    url(r'^recipes', views.Recommend_recipes.as_view()),
    url(r'^final', views.Final_recipes.as_view()),
]