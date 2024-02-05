from django.db import models

class School(models.Model):
    name = models.CharField(max_length=50)
    slogan = models.CharField(max_length=50, blank=True, null=True)
    adress = models.CharField(max_length=50, blank=True, null=True)
    pobox = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
