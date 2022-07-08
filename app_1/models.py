# Create your models here.
from django.db import models

from dataclasses import dataclass
from django.db import models


# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    c=models.CharField(max_length=200)
    age=models.CharField(max_length=200)

class contactus(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    comment=models.CharField(max_length=200)