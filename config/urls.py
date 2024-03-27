"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.shortcuts import render, redirect
from workout.models import Excercise, TrainingEvent

def indexPage(request):
    excercises = Excercise.objects.all() # ⭐ SQL Magic ✨
    events = TrainingEvent.objects.all() # ⭐ More SQL Magic ✨
    return render(
        request, 
        'index.html', 
        {"excercises": excercises, "events":events}
    )

def addNew(request):
    excercise = Excercise.objects.get(id = request.POST['excercise'])
    date = request.POST['date']
    reps = request.POST['reps']
    weight = request.POST['weight']
    event = TrainingEvent( 
        excercise = excercise, 
        date = date, 
        reps = reps, 
        weight = weight )
    event.save()
    return redirect('index')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage, name="index"),
    path('newEvent/', addNew, name="add")
]
