from django.shortcuts import render
from django.http import HttpResponse

from .models import RecipeIngredient, Ingredient, Recipe

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'

#def recipes(request):
#    recipes = Recipe.objects.all()
#    ctx = { "recipes": recipes }
#    return render(request, 'ledger/recipes_list.html', ctx)

#def recipe_detail(request, pk):
#    ctx = {'recipe': Ingredient.objects.filter(recipe__recipe__name=pk)}
#    
#    return render(request, 'ledger/recipe_detail.html', ctx)