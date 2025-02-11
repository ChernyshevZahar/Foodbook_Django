from django.urls import path
from .views import RecipeListView , RecipeDitailsView, CreateRecipteView

app_name='RecipeAndProduct'

urlpatterns = [
    path('recipts/', RecipeListView.as_view(), name = 'recipt-list'),
    path('recipts/<int:pk>', RecipeDitailsView.as_view(), name = 'recipt-ditails'),
    path('recipts/create', CreateRecipteView.as_view(), name = 'recipt-add')

]