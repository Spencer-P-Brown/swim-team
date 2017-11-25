from django.db import models

# Create your models here.
class Measurement(models.Model):
    rpe = models.IntegerField()
    excersize = models.CharField(max_length=250)
    
