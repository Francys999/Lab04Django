from django.shortcuts import render, redirect, get_object_or_404
from .models import Exercise
from .forms import ExerciseForm
import matplotlib.pyplot as plt
import io
import base64
from django.http import HttpResponse
import numpy as np

# Vista de la página principal con análisis de rendimiento
def home(request):
    exercises = Exercise.objects.all()  # Obtener todos los ejercicios registrados

    # Calcular las métricas de rendimiento
    if exercises:
        # Extraemos las listas de datos necesarios para los gráficos
        dates = [exercise.date for exercise in exercises]
        distances = [exercise.distance for exercise in exercises]
        durations = [exercise.duration for exercise in exercises]
        calories = [exercise.calories_burned for exercise in exercises]

        # Calculamos promedios
        avg_distance = np.mean(distances) if distances else 0
        avg_duration = np.mean(durations) if durations else 0
        avg_calories = np.mean(calories) if calories else 0

        # Crear gráfico de rendimiento (por ejemplo, comparación de distancia y duración)
        fig, ax = plt.subplots()
        ax.plot(dates, distances, label="Distancia (km)", color='blue', marker='o')
        ax.plot(dates, durations, label="Duración (min)", color='green', marker='o')
        ax.set_xlabel('Fecha')
        ax.set_ylabel('Valor')
        ax.set_title('Rendimiento de Ejercicios: Distancia vs Duración')
        ax.legend()

        # Guardar el gráfico en un buffer de memoria
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()

        # Pasar la imagen base64 y las métricas al template
        context = {
            'exercises': exercises,
            'avg_distance': avg_distance,
            'avg_duration': avg_duration,
            'avg_calories': avg_calories,
            'chart': image_base64,  # Imagen en base64 para mostrar en el template
        }

        return render(request, 'exercise_tracker/home.html', context)
    
    # Si no hay ejercicios registrados
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

# Vista para editar un ejercicio
def edit_exercise(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)

    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir a la página principal después de guardar
    else:
        form = ExerciseForm(instance=exercise)

    return render(request, 'exercise_tracker/edit_exercise.html', {'form': form})

# Vista para eliminar un ejercicio
def delete_exercise(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)

    if request.method == "POST":
        exercise.delete()
        return redirect('home')  # Redirigir a la página principal después de eliminar

    return render(request, 'exercise_tracker/delete_exercise.html', {'exercise': exercise})
