from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField(max_length=30)
    mbl = models.CharField(max_length=10)
    add = models.TextField()
    def __str__(self):
        return f"{self.name} {self.roll} {self.age} {self.email} {self.mbl} {self.add}"
