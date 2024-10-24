from django.contrib import admin
from .models import Horse, Care, Training

@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'health_status', 'last_vet_check')

@admin.register(Care)
class CareAdmin(admin.ModelAdmin):
    list_display = ('horse', 'care_type', 'date')

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('horse', 'training_type', 'duration', 'date')

