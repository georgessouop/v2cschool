from django.db import models
from django.utils import timezone

from school.models import School
from classes.models import Classe

class Student(models.Model):
    CHOICES = [
        ('girl', 'Fille'),
        ('boy', 'Garçon')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField()
    date_joined = models.DateField(default=timezone.now)
    matricule = models.CharField(max_length=50)
    town = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, choices=CHOICES)
    photo = models.ImageField(default='default.jpg', upload_to='students_pics')
    active = models.BooleanField(default=True)
    parent_name = models.CharField(max_length=50)
    parent_phone = models.CharField(max_length=50)
    parent_email = models.CharField(max_length=50, blank=True, null=True)
    observations = models.TextField()
    
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

