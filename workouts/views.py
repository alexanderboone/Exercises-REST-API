from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Exercise
from .forms import ExerciseForm

def home_view(request):
    return render(request, "home.html", {})

def exercise_list_view(request):
    queryset = Exercise.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "workouts/exercise_list.html", context)

def exercise_detail_view(request, exercise_name):
    obj = get_object_or_404(Exercise, name__iexact=exercise_name.replace('-', ' '))
    context = {
        'object': obj
    }
    return render(request, "workouts/exercise_detail.html", context)

def exercise_create_view(request):
    form = ExerciseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ExerciseForm()
    context = {
        'form': form
    }
    return render(request, "workouts/exercise_create.html", context)

def workout_list_view(request):
    return render(request, "workouts/workout_list.html", {})