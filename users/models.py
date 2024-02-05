from django.db import models
from django.contrib.auth.models import AbstractUser

from school.models import School

class User(AbstractUser):
    phone = models.CharField(max_length=50, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        permissions = []

# Add related_name to groups and user_permissions fields
User._meta.get_field('groups').remote_field.related_name = 'user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'user_permissions_set'


class Profile(models.Model):
    CHOICES = [
        ('admin', 'Administrateur'),
        ('teacher', 'Enseignant')
    ]
    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(max_length=50, choices=CHOICES, default='admin')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    # @property
    # def display_role(self):
    #     return dict(self.CHOICES).get(self.role, 'Undefined')
