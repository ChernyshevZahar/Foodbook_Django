from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserAndProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'Электронная почта'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        if self.instance.pk:
            self.fields['bio'] = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), label='О себе', required=False, max_length=500)
            self.fields['argumet_acsepted'] = forms.BooleanField(label='Соглашение', required=False)
            self.fields['avatar'] = forms.ImageField(label='Аватар', required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
