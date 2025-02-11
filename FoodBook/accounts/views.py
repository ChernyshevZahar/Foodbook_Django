from django.shortcuts import render
from .forms import ProfileEditForm
from .models import Profile

from django.contrib.auth import authenticate, login

from  django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from  django.urls import reverse_lazy

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register_user.html"
    success_url = reverse_lazy('RecipeAndProduct:recipt-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(
            self.request,
            username=username,
            password=password,

        )
        login(request=self.request, user=user)
        return response

class AboutMeView(TemplateView):
    template_name = 'accounts/about-my.html'

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login_app')
