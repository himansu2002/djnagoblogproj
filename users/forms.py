from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class userUpdateform(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email']


class profileupdateform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

