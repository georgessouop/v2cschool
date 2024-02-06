from django.db import models
from django.contrib.auth.models import AbstractUser

from school.models import School

class User(AbstractUser):
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
