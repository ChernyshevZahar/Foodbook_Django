from django.contrib import admin
from .models import CatigoryRecipe, Recipe, Products



class CatigoryRecipeInLine(admin.TabularInline):
    model = CatigoryRecipe.orders.through

class ProductsInLine(admin.TabularInline):
    model = Products.orders.through
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        CatigoryRecipeInLine,
        ProductsInLine,
    ]
    list_display = ["name","discription","cooking_steps","cooking_time","image_dish"]

@admin.register(CatigoryRecipe)
class CatigoryRecipeAdmin(admin.ModelAdmin):
    list_display = ["name",]

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name","price", "callorise"]
