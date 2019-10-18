from django.db import models

# Create your models here.
class InCharge(models.Model):
    inChargeName = models.CharField(max_length=150)
    def __str__(self):
        return '{}'.format(self.inChargeName)