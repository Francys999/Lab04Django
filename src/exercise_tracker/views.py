from django.shortcuts import render, redirect
from .models import Exercise
from .forms import ExerciseForm

def home(request):
    exercises = Exercise.objects.all()  # Obtener todos los ejercicios registrados
    return render(request, 'exercise_tracker/home.html', {'exercises': exercises})

def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo ejercicio en la base de datos
            return redirect('home')  # Redirigir a la página principal después de guardar
    else:
        form = ExerciseForm()
    return render(request, 'exercise_tracker/add_exercise.html', {'form': form})

