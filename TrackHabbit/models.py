from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.

class User(AbstractUser):
    pass

class Habit(models.Model):
    name = models.CharField(max_length=255)
    metric = models.PositiveIntegerField()
    unit_of_measure = models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DailyRecord(models.Model):
    habit_key=models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='records')
    date=models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Record for {self.habit.name}"
