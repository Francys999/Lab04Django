from django.shortcuts import render, redirect, get_object_or_404
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
