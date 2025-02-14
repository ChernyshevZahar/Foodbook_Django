from django import forms
from django.core.exceptions import ValidationError
from .models import Recipe

class AddingRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название блюда'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание', 'rows': 4}),
            'cooking_steps': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Шаги приготовления', 'rows': 6}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Время приготовления (минуты)'}),
            'image_dish': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
          'name': 'Название блюда',
          'discription': 'Описание',
          'cooking_steps': 'Шаги приготовления',
          'cooking_time': 'Время приготовления (минуты)',
          'image_dish': 'Фотография блюда',
          'catigory_recipe': 'Категории',
          'products': 'Ингредиенты',
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name:
            raise ValidationError('Пожалуйста, введите название блюда.')
        return name

    def clean_discription(self):
        description = self.cleaned_data['discription']
        if not description:
            raise ValidationError('Пожалуйста, введите описание блюда.')
        return description

    def clean_cooking_steps(self):
        steps = self.cleaned_data['cooking_steps']
        if not steps:
            raise ValidationError('Пожалуйста, введите шаги приготовления.')
        return steps

    def clean_cooking_time(self):
        cooking_time = self.cleaned_data['cooking_time']
        if cooking_time < 1:
            raise ValidationError('Время приготовления должно быть больше 0 минут.')
        return cooking_time


class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'discription', 'cooking_steps', 'cooking_time', 'image_dish', 'catigory_recipe', 'products']  # Include all relevant fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название блюда'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Описание'}),
            'cooking_steps': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Шаги приготовления'}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Время приготовления (минуты)'}),
            'image_dish': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'catigory_recipe': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'products': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


