from django.shortcuts import render
from django.views.generic import ListView , DetailView

from .models import Recipe

class RecipeListView(ListView):
    template_name = "RecipeAndProduct/recipe_list.html"
    queryset = (
        Recipe.objects
        .prefetch_related('catigory_recipe',)
        .all()
    )
    context_object_name = 'listrecipte'


class RecipeDitailsView(DetailView):
    template_name = "RecipeAndProduct/recipe-ditails.html"
    queryset = (
        Recipe.objects
        .prefetch_related('catigory_recipe', )
        .all()
    )
    context_object_name = 'recept'
