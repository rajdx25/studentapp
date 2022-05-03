from django.db import models

# Create your models here.

class Permission(models.Model):
    empcode=models.IntegerField()
    username=models.CharField(max_length=50,default='')
    password=models.CharField(max_length=50,default='')
    is_active=models.ImageField(null=True)
    
