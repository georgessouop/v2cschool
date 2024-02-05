from django.db import models

from school.models import School

class Classe(models.Model):
    section = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=50, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
