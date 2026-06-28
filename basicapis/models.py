from django.db import models


# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=60)
    Age = models.IntegerField(default=18)
