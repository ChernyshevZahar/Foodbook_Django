from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView

from django.urls import reverse_lazy

from .models import Recipe
from .forms import AddingRecipeForm
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

class CreateRecipteView(CreateView):
    template_name = "RecipeAndProduct/recipe-adding.html"
    form_class = AddingRecipeForm
    success_url = reverse_lazy('RecipeAndProduct:recipt-list')
    def form_valid(self, form):
        recipte = form.save(commit=False)
        recipte.save()
        return super().form_valid(form)
