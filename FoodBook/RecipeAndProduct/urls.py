from django.urls import path
from .views import RecipeListView , RecipeDitailsView, CreateRecipteView, UpdateRecipteView, DeleteRecipteView

app_name='RecipeAndProduct'

urlpatterns = [
    path('recipts/', RecipeListView.as_view(), name = 'recipt-list'),
    path('recipts/<int:pk>', RecipeDitailsView.as_view(), name = 'recipt-ditails'),
    path('recipts/<int:pk>/update', UpdateRecipteView.as_view(), name = 'recipt-update'),
    path('recipts/<int:pk>/delete', DeleteRecipteView.as_view(), name = 'recipt-delete'),
    path('recipts/create', CreateRecipteView.as_view(), name = 'recipt-add')

]