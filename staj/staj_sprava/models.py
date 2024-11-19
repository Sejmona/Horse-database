from django.db import models
from django.contrib.auth.models import User

class Horse(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    health_status = models.TextField()  # Zdravotní stav koně
    last_vet_check = models.DateField(null=True, blank=True, verbose_name="Poslední kontrola veterináře")  # Datum poslední veterinární prohlídky
    notes = models.TextField(blank=True, null=True)  # Poznámky
    user = models.ForeignKey(User, on_delete=models.CASCADE) # další pole pro koně
    

    def __str__(self):
        return self.name

class Care(models.Model):
    CARE_CHOICES = [
        ('Feeding', 'Krmení'),
        ('Grooming', 'Čištění'),
        ('Veterinary', 'Veterinář'),
    ]
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE, related_name="care_sessions")  # Vztah k modelu Horse
    care_type = models.CharField(max_length=50, choices=CARE_CHOICES)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_care_type_display()} for {self.horse.name} on {self.date}"

class Training(models.Model):
    TRAINING_CHOICES = [
        ('Riding', 'Jízda'),
        ('Jumping', 'Skoky'),
        ('Conditioning', 'Kondiční trénink'),
    ]
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE, related_name="trainings")
    training_type = models.CharField(max_length=50, choices=TRAINING_CHOICES)
    duration = models.DurationField()  # Doba tréninku
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.get_training_type_display()} with {self.horse.name} on {self.date}"

