from django.urls import path

from django.contrib.auth.views import LoginView
from .views import MyLogoutView,RegisterUser,AboutMeView

app_name='accounts'

urlpatterns = [
    path('login/', LoginView.as_view(
            template_name='accounts/login_myauth.html',

        ), name='login_app'),
    path('logout/', MyLogoutView.as_view(), name='Logout_app'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('about-me/', AboutMeView.as_view(), name='about_me'),
]