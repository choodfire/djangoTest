import django.utils.timezone
from django.db import models
import datetime

# Create your models here.
class Employee(models.Model):
    name = models.CharField(default='noname', max_length=100)
    title = models.CharField(max_length=100)
    joinDate = models.DateField(default=django.utils.timezone.now())

    def __str__(self):
        return f"{self.name} - {self.title}"