from django.db import models

from users.views import User


# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    ]

    STATUS_CHOICES =[
        ('pending','Pending'),
        ('in_progress','In Progress'),
        ('completed','Completed'),
    ]


    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

