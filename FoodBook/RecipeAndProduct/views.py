from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy,reverse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import Recipe
from .forms import AddingRecipeForm , RecipeUpdateForm
class RecipeListView(ListView):
    template_name = "RecipeAndProduct/recipe_list.html"
    queryset = (
        Recipe.objects
        .prefetch_related('catigory_recipe',)
        .all()
    )
    context_object_name = 'listrecipte'




class RecipeDitailsView( DetailView):
    template_name = "RecipeAndProduct/recipe-ditails.html"
    queryset = (
        Recipe.objects
        .prefetch_related('catigory_recipe', )
        .all()
    )
    context_object_name = 'recept'



class CreateRecipteView(LoginRequiredMixin,CreateView):
    template_name = "RecipeAndProduct/recipe-adding.html"
    form_class = AddingRecipeForm
    success_url = reverse_lazy('RecipeAndProduct:recipt-list')
    def form_valid(self, form):
        user = self.request.user
        recipte = form.save(commit=False)
        recipte.user = user
        recipte.save()
        return super().form_valid(form)

class UpdateRecipteView(LoginRequiredMixin,UpdateView):
    template_name = "RecipeAndProduct/recipe-update.html"
    model = Recipe
    form_class = RecipeUpdateForm  # Используем кастомную форму

    def get_success_url(self):
        return reverse(
            'RecipeAndProduct:recipt-ditails',
            kwargs={'pk': self.object.pk}
        )

class DeleteRecipteView(LoginRequiredMixin,DeleteView):
    model =  Recipe
    success_url = reverse_lazy('RecipeAndProduct:recipt-list')
