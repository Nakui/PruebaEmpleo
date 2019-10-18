from django.db import models
from inCharge.models import InCharge


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=150)
    date_of_delivery = models.DateField()
    description = models.CharField(max_length=150)
    inCharge = models.ForeignKey(InCharge, null=True, blank=True, on_delete=models.CASCADE)