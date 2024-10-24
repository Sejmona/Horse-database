from django.shortcuts import render, redirect
from .forms import HorseForm, CareForm, TrainingForm

def add_horse(request):
    if request.method == 'POST':
        form = HorseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horse_list')  # Přesměrování na seznam koní po úspěšném přidání
    else:
        form = HorseForm()
    return render(request, 'staj_sprava/add_horse.html', {'form': form})

def add_care(request):
    if request.method == 'POST':
        form = CareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horse_list')  # Přesměrování na seznam koní po přidání péče
    else:
        form = CareForm()
    return render(request, 'staj_sprava/add_care.html', {'form': form})

def add_training(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horse_list')  # Přesměrování na seznam koní po přidání tréninku
    else:
        form = TrainingForm()
    return render(request, 'staj_sprava/add_training.html', {'form': form})

