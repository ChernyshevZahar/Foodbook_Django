from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy,reverse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

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

    @method_decorator(cache_page(60 * 3))  # Cache for 1 hour
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


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
        user = self.request.user
        recipte = form.save(commit=False)
        recipte.user = user
        recipte.save()
        return super().form_valid(form)

class UpdateRecipteView(UpdateView):
    template_name = "RecipeAndProduct/recipe-update.html"
    model = Recipe
    fields = ['discription','image_dish','catigory_recipe']

    def get_success_url(self):
        return reverse(
            'RecipeAndProduct:recipt-ditails',
            kwargs= {'pk': self.object.pk}

        )

class DeleteRecipteView(DeleteView):
    model =  Recipe
    success_url = reverse_lazy('RecipeAndProduct:recipt-list')
