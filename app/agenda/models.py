from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    fone = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Profissional(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    services = models.ManyToManyField('Service', related_name='services')

    def __str__(self):
        return self.name

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    time_min = models.IntegerField()


    def __str__(self):
        return self.description

class Events(models.Model):
    id = models.AutoField(primary_key=True)    
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default='1')
    professional = models.ForeignKey(Profissional, on_delete=models.CASCADE, default='1')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default='1')
    observation = models.TextField(null=True,blank=True)