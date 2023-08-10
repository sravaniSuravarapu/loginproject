from django.db import models

# Create your models here.
class studentgrp(models.Model):
    fname = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    ph_no = models.IntegerField(default=0)
    def __str__(self):
        return self.fname