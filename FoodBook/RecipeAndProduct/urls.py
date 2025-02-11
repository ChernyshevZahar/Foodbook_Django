from django.urls import path
from .views import RecipeListView

app_name='RecipeAndProduct'

urlpatterns = [
    path('recipts/', RecipeListView.as_view(), name = 'recipt-list')
]