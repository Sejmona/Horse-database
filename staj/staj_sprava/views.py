from django.shortcuts import render, redirect, get_object_or_404
from .forms import HorseForm, CareForm, TrainingForm
from .models import Horse
from django.shortcuts import get_object_or_404


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
  
def horse_list(request):
    horses = Horse.objects.all()  # Načte všechny koně z databáze
    return render(request, 'staj_sprava/horse_list.html', {'horses': horses})
  
def horse_detail(request, horse_id):
    horse = get_object_or_404(Horse, id=horse_id)
    return render(request, 'staj_sprava/horse_detail.html', {'horse': horse})
  
def home(request):
    return render(request, 'staj_sprava/home.html')
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Horse

def horse_detail(request, horse_id):
    horse = get_object_or_404(Horse, id=horse_id)
    trainings = horse.trainings.all()
    care_sessions = horse.care_sessions.all()
    return render(request, 'staj_sprava/horse_detail.html', {
        'horse': horse,
        'trainings': trainings,
        'care_sessions': care_sessions
    })
    
def delete_horse(request, horse_id):
    horse = get_object_or_404(Horse, id=horse_id)
    horse.delete()
    return redirect('horse_list')  # Předpokládáme, že 'horse_list' je název URL pro seznam koní


