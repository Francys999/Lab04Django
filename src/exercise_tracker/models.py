from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)  # Ejemplo: Correr, Sentadillas, etc.
    duration = models.DecimalField(max_digits=5, decimal_places=2)  # Duración en minutos
    distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Distancia en km
    calories_burned = models.DecimalField(max_digits=6, decimal_places=2)  # Calorías quemadas
    date = models.DateTimeField(auto_now_add=True)  # Fecha y hora en la que se registró el ejercicio

    def __str__(self):
        return f'{self.name} - {self.date}'
