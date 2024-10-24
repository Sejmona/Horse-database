from django import forms
from .models import Horse, Care, Training

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
