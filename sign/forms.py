from django import forms
from django.contrib.auth.models import User
from sign.models import UserInfoForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserInfoForm
        fields = ('portpolio_site', 'profile_img')