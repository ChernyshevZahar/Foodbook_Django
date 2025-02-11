from django import forms

from  .models import Recipe

class AddingRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('user',)