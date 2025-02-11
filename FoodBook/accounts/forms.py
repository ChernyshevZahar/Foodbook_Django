from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserAndProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email') # Поля модели User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'Электронная почта'
        if self.instance.pk:  #Только для существующих пользователей
            self.fields['bio'] = forms.CharField(widget=forms.Textarea, label='О себе', required=False, max_length=500)
            self.fields['argumet_acsepted'] = forms.BooleanField(label='Соглашение', required=False)
            self.fields['avatar'] = forms.ImageField(label='Аватар', required=False)