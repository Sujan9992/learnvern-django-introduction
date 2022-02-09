from pyexpat import model
from django.db import models

# Create your models here.
class Teacher(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.FirstName