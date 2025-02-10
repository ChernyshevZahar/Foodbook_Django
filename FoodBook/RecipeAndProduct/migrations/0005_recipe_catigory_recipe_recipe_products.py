# Generated by Django 5.1.6 on 2025-02-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeAndProduct', '0004_recipe_image_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='catigory_recipe',
            field=models.ManyToManyField(related_name='catigory_recipe', to='RecipeAndProduct.catigoryrecipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(related_name='products', to='RecipeAndProduct.products'),
        ),
    ]
