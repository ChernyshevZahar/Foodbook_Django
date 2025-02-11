from django.shortcuts import render
from .models import Profile

from django.contrib.auth import authenticate, login

from  django.views.generic import CreateView, TemplateView , UpdateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from  django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserAndProfileForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

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

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserAndProfileForm
    template_name = 'accounts/profile_update.html' # Замените на имя вашего шаблона
    success_url = reverse_lazy('accounts:about_me')

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        profile, created = Profile.objects.get_or_create(user=user)
        profile.bio = form.cleaned_data.get('bio')
        profile.argumet_acsepted = form.cleaned_data.get('argumet_acsepted')
        profile.avatar = form.cleaned_data.get('avatar')
        profile.save()
        return super().form_valid(form)
