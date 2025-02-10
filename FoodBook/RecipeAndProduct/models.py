from django.db import models


def image_path_name(instens:'Recipe', filename:str) -> str:
    return "dish/dish_{pk}/image/{filename}".format(
        pk=instens.pk,
        filename=filename,
    )
class Products(models.Model):
    name = models.CharField(max_length=30,blank=True)
    price = models.DecimalField(default=0,max_digits=8,decimal_places=2)
    callorise = models.IntegerField(null=False, blank=True)

    def __str__(self):
        return f"{self.name}"


class CatigoryRecipe(models.Model):
    name = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return f"{self.name}"

class Recipe(models.Model):
    name = models.CharField(max_length=30,blank=True)
    discription  = models.TextField(null=False,blank=True)
    cooking_steps = models.TextField(null=False,blank=True)
    cooking_time = models.PositiveSmallIntegerField(default=0)
    image_dish  = models.ImageField(null=True, blank=True, upload_to=image_path_name)
    catigory_recipe = models.ManyToManyField(CatigoryRecipe, related_name='catigory_recipe')
    products = models.ManyToManyField(Products, related_name='products')