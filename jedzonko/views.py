from datetime import datetime
import random
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib import messages

from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import (
    Recipe,
    RecipePlan,
    DayName,
    Plan,
    Page
)
from django.template.defaulttags import register



class IndexView(View):

    def landing(request):
        return render(request, 'jedzonko/index.html')

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "jedzonko/test.html", ctx)

    def carousel(request):
        recipes = Recipe.objects.order_by('?')[:3]
        context = {
            "first": recipes[0],
            "second": recipes[1],
            "third": recipes[2],
        }
        return render(request, 'jedzonko/index.html', context)

    def dashboard(request):
        if request.method == "GET":
            all_plans = Plan.objects.all().order_by('-created')
            last_plan = all_plans[0]
            plans_quantity = all_plans.count()
            recipe_quantity = Recipe.objects.all().count()
            recipe_plan = RecipePlan.objects.filter(plan=last_plan.id).order_by('day_name__order', 'order')
            recipe_plan_by_day = {}
            for element in recipe_plan:
                if element.day_name.day_name in recipe_plan_by_day:
                    recipe_plan_by_day[element.day_name.day_name].append(element)
                else:
                    recipe_plan_by_day[element.day_name.day_name] = [element]
            ctx = {"last_plan": last_plan,
                   "recipe_plan_by_day": recipe_plan_by_day,
                   "plans_quantity": plans_quantity,
                   "recipe_quantity": recipe_quantity,
                   }
        return render(request, 'jedzonko/dashboard.html', ctx)


    def about(request):
        return render(request, 'jedzonko/about.html')

    def contact(request):
        return render(request, 'jedzonko/contact.html')

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

class RecipeView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "jedzonko/test.html", ctx)

    def recipe_list(request):
        recipe_list = Recipe.objects.all()
        ctx = {'recipe': recipe_list}
        return render(request, 'jedzonko/app-recipes.html', ctx)

    def add_recipe(request):

        if request.method == "POST":
            name = request.POST['name']
            description = request.POST['description']
            preparation_time = request.POST['preparation_time']
            ingredients = request.POST['ingredients']
            preparation = request.POST['preparation']
            if name and description and preparation_time and ingredients and preparation:
                Recipe.objects.create(
                    name = name,
                    ingredients = ingredients,
                    description = description,
                    preparation_time = preparation_time,
                    preparation = preparation
                )
                messages.add_message(request, messages.INFO, "Przepis dodano pomyślnie")
                return redirect('/recipe/list/')
            else:
                messages.add_message(request, messages.INFO, "Wypełnij poprawnie wszystkie pola")
                return redirect('/recipe/add/')
        return render(request, 'jedzonko/app-add-recipe.html')

    def recipe_details(request, id):
        recipe = Recipe.objects.get(id=id)
        ctx = {'recipe': recipe}
        return render(request, 'jedzonko/app-recipe-details.html', ctx)

    def modify(request, id):
        return render(request, 'jedzonko/app-edit-recipe.html')

class PlanView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "jedzonko/test.html", ctx)

    def plan_add_details(request):
        ctx = {
            "plan": Plan.objects.latest('id')
        }
        return render(request, 'jedzonko/app-details-schedules.html', ctx)


class RecipeListView(ListView):
    model = Recipe
    template_name = 'jedzonko/recipes.html'
    context_object_name = 'Recipe'
    # ordering = ['votes'] - alternative but only one fiter available;
    paginate_by = 5

    def get_queryset(self):
        queryset = Recipe.objects.order_by('-created').order_by('-votes')
        return queryset



class PlanListView(ListView):
    model = Plan
    template_name = 'jedzonko/app-schedules.html'
    context_object_name = 'plan'
    ordering = ['name']
    paginate_by = 5




class AddPlan(View):

    def get(self, request):
        return render(request, "jedzonko/app-add-schedules.html")

    def post(self, request):
        name = request.POST.get("name")
        description = request.POST.get("description")
        if name and description:
            new_plan = Plan.objects.create(name=name, description=description)
            request.session['plan_id'] = new_plan.id
            messages.add_message(request, messages.INFO, "Plan dodano pomyślnie")
            return redirect('/plan/add/details')
        else:
            messages.add_message(request, messages.INFO, "Uzupełnij wszystkie pola poprawnie!")
            return redirect('/plan/add/')


class RecipeDetails(View):

    def get(self, request, id):
        recipe = Recipe.objects.get(pk=id)
        ctx = {
            "recipe": recipe,
        }
        return render(request, "jedzonko/recipe-details.html", ctx)

class PlanDetails(View):

    def get(self, request, id):
        plan = Plan.objects.get(pk=id)
        recipe_plan = RecipePlan.objects.filter(plan=plan.id).order_by('day_name__order', 'order')
        recipe_plan_by_day = {}
        for element in recipe_plan:
            if element.day_name.day_name in recipe_plan_by_day:
                recipe_plan_by_day[element.day_name.day_name].append(element)
            else:
                recipe_plan_by_day[element.day_name.day_name] = [element]
        ctx = {
            "plan": plan,
            "recipe_plan_by_day": recipe_plan_by_day,
        }
        return render(request, "jedzonko/app-details-schedules.html", ctx)


    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)
