from django.db import models

# Create your models here.

class student(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    roll_no = models.IntegerField
    ph_no = models.IntegerField