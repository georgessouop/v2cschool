from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from school.models import School

class User(AbstractUser):
    CHOICES = [
        ('girl', 'Fille'),
        ('boy', 'Garçon')
    ]

    birth_date = models.DateField(blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, choices=CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Profile(models.Model):
    CHOICES = [
        ('admin', 'Administrateur'),
        ('teacher', 'Enseignant')
    ]
    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(max_length=50, choices=CHOICES, default='admin')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.role
