from django.db import models

# Create your models here.
class Student(models.Model):
    studentname=models.CharField(max_length=100)
    studentaddress=models.CharField(max_length=200)
    studentnumber=models.IntegerField()
    studentemail=models.EmailField(max_length=100)