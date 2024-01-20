from django.db import models

# Create your models here.


class country(models.Model):
    Ccname=models.CharField(max_length=100,primary_key=100)
    