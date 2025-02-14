from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserAndProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            if self.fields[field_name].label == "Электронная почта":
              self.fields[field_name].widget.attrs['type'] = 'email'

        if self.instance and self.instance.pk:
            self.fields['bio'] = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
                                                 label='О себе', required=False, initial=self.instance.profile.bio,
                                                 max_length=500)
            self.fields['argumet_acsepted'] = forms.BooleanField(label='Соглашение', required=False,
                                                                 initial=self.instance.profile.argumet_acsepted)
            if self.instance.profile.avatar:
                self.fields['avatar'] = forms.ImageField(label='Аватар', required=False,
                                                         initial=self.instance.profile.avatar.url,
                                                         widget=forms.ClearableFileInput(
                                                             attrs={'class': 'form-control-file'}))
            else:
                self.fields['avatar'] = forms.ImageField(label='Аватар', required=False,
                                                         widget=forms.ClearableFileInput(
                                                             attrs={'class': 'form-control-file'}))