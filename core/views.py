from django.shortcuts import render, get_object_or_404
from .models import Trail, Exercise

def home(request):
    return render(request, 'core/home.html')

def trails(request):
    all_trails = Trail.objects.all()
    return render(request, 'core/trails.html', {'trails': all_trails})

def exercises(request, trail_id):
    trail = get_object_or_404(Trail, id=trail_id)
    exercises = Exercise.objects.filter(trail=trail)
    return render(request, 'core/exercises.html', {'exercises': exercises})

def trails(request):
    all_trails = Trail.objects.all()
    return render(request, 'core/trails.html', {'trails': all_trails})