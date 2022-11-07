import resource
from django.shortcuts import render, redirect
from . import models
from .models import User, Habit, DailyRecord
from django.contrib.auth.decorators import login_required
from .forms import HabitForm
from datetime import datetime
# Create your views here.

@login_required
def index(request):
    habits = Habit.objects.order_by('created_at')
    records = DailyRecord.objects.order_by("date")
    return render(request, 'TrackHabit/index.html', {'habits':habits, 'records':records})

def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect("home")
    else:
        form = HabitForm()
    return render(request, 'TrackHabit/create_habit.html', {'form': form})

def edit_habit(request, habit_id):
    habit = Habit.objects.get(pk=habit_id)
    form = HabitForm(request.POST or None, instance=habit)
    if form.is_valid():
        resource = form.save()
        return redirect("home")
    return render(request, 'TrackHabit/edit_habit.html', {'habit': habit, 'form':form})

def delete_habit(request, habit_id):
    habit = Habit.objects.get(pk=habit_id)
    habit.delete()
    return redirect("home")

def view_habit(request, habit_id):
    habit = Habit.objects.get(pk=habit_id)
    records = DailyRecord.objects.filter(habit_key = habit_id).order_by('date')
    return render(request, 'TrackHabit/habit_detail.html' ,{'habit': habit, 'records':records})

def create_record(request, habit_id):
    habit = Habit.objects.get(pk=habit_id)
    records = DailyRecord.objects.filter(habit_key = habit_id).order_by('date')
    record = models.DailyRecord(habit_key = habit, date = datetime.now())
    record.save()
    return render(request, 'TrackHabit/habit_detail.html' ,{'habit': habit, 'records':records})
    # if(habit.count > 0):
    #     date = records.objects.latest('date')
    #     day = date.day + 1 
    #     record = models.DailyRecord(habit_key=habit, date= )
    #     record.save()
    # else:
    #     record = models.DailyRecord(habit_key = Habit, date = datetime.now())
    #     record.save()
