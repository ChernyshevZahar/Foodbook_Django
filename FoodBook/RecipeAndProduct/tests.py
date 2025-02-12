from http.client import responses
from django.contrib.auth.models import User
from django.test import TestCase
from  .models import Recipe
from django.urls import reverse

class TecipeDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.User = User.objects.create_user(username="bob", password='12345')

    @classmethod
    def tearDownClass(cls):
        cls.User.delete()

    def setUp(self) -> None:
        self.client.force_login(self.User)
        self.recipe = Recipe.objects.create(
            name='test',
            discription = 'wdfwe',
            cooking_steps = '1.2.3.4',
            cooking_time = 30,
            user = self.User
        )

    def tearDown(self):
        self.recipe.delete()

    def test_recipe_details(self):
        respons = self.client.get(reverse('RecipeAndProduct:recipt-list'))
        self.assertContains(respons, self.recipe.name)
        self.assertContains(respons, self.recipe.cooking_time)
        self.assertContains(respons, self.recipe.pk)
