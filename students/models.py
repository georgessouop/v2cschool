from django.db import models
from django.utils import timezone

from school.models import School
from classes.models import Classe

class Student(models.Model):
    CHOICES = [
        ('girl', 'Fille'),
        ('boy', 'Garçon')
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    entry_date = models.DateField(default=timezone.now)
    sex = models.CharField(max_length=10, choices=CHOICES)
    registration_number = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(default=True)
    
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

