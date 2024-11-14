from django import forms
from .models import Horse, Care, Training
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Jméno uživatele")
    password = forms.CharField(widget=forms.PasswordInput, label="Heslo")

class HorseForm(forms.ModelForm):
    class Meta:
        model = Horse
        fields = ['name', 'breed', 'age', 'health_status', 'last_vet_check', 'notes']

class CareForm(forms.ModelForm):
    class Meta:
        model = Care
        fields = ['horse', 'care_type', 'date', 'notes']

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['horse', 'training_type', 'duration', 'date', 'notes']
