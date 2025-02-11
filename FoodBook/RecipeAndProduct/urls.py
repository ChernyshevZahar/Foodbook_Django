from django.urls import path
from .views import RecipeListView , RecipeDitailsView

app_name='RecipeAndProduct'

urlpatterns = [
    path('recipts/', RecipeListView.as_view(), name = 'recipt-list'),
    path('recipts/<int:pk>', RecipeDitailsView.as_view(), name = 'recipt-ditails')
]