from django.db import models

from school.models import School

class Subject(models.Model):
    label = models.CharField(max_length=50, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
