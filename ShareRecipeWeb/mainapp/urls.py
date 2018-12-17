from django.urls import path,re_path
from django.conf import urls
from mainapp.views import index , signup , post_signup , post_logout , post_login
from recipe.views import get_recipes_api , get_create_recipe , post_create_recipe , get_recipe 


urlpatterns = [
    path("", index, name="index"),
    path("signup/",signup,name="signup"),
    path("signup/post",post_signup,name="post_signup"),
    path("logout/post",post_logout,name="post_logout"),
    path("login/post",post_login,name="post_login"),
    path("api/recipes",get_recipes_api,name="get_recipes_api" ),
    path("recipes/create/",get_create_recipe,name="get_create_recipe"),
    path("recipes/post",post_create_recipe,name="post_create_recipe"),
    path('recipes/<int:recipe_id>/',get_recipe,name="get_recipe"),
   
]