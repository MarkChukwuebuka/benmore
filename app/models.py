from django.db import models
from django.contrib.auth.models import User

class StatusChoices(models.TextChoices):
    in_progress = 'In Progress'
    completed = 'Completed'
    overdue = 'Overdue'

class PriorityChoices(models.TextChoices):
    low = 'Low'
    medium = 'Medium'
    high = 'High'



class Task(models.Model):
    
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=StatusChoices.choices)
    priority = models.CharField(max_length=20, choices=PriorityChoices.choices)
    due_date = models.DateTimeField()
    category = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
