"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from jedzonko.views import IndexView, RecipeView, PlanView, RecipeListView, AddPlan, RecipeDetails, PlanDetails, PlanListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', IndexView.as_view()),
    path('', IndexView.carousel, name="landing page"),
    path('main/', IndexView.dashboard, name="dashboard"),
    path('about/', IndexView.about, name="about"),
    path('contact/', IndexView.contact, name="contact"),
    path('recipe/', RecipeView.as_view()),
    # path('recipe/list/', RecipeView.recipe_list, name="recipe list"),
    path('recipe/add/', RecipeView.add_recipe, name="add recipe"),
    # re_path(r'recipe/(?P<id>\d+)/$', RecipeView.recipe_details, name="recipe details"),
    # path('recipe/<int:id>', RecipeView.recipe_details, name="recipe details"),
    re_path(r'recipe/modify/(?P<id>\d+)/$', RecipeView.modify, name="recipe modify"),
    path('plan/', PlanView.as_view()),
    re_path(r'plan/(?P<id>\d+)/$', PlanDetails.as_view(), name="plan details"),
    # path('plan/add/', PlanView.add_plan, name="add plan"),
    path('plan/add/details', PlanView.plan_add_details, name="add plan details"),
    path('recipe/list/', RecipeListView.as_view(), name="RecipeListView"),
    path('plan/add/', AddPlan.as_view(), name="add plan"),
    re_path(r'recipe/(?P<id>\d+)/$', RecipeDetails.as_view(),  name="recipe details"),
    path('plan/list/', PlanListView.as_view(), name="plan list"),

]
