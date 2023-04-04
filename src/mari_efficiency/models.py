from django.db import models

# Create your models here.
class Item(models.Model):


    name = models.CharField(default='', max_length=50, unique=True)
    cost = models.DecimalField(default='', max_digits=5, decimal_places=0)
    quantity = models.DecimalField(default='', max_digits=5, decimal_places=0)
    type = models.CharField(max_length=20, default='', choices=[('ENH', 'Enhancement'), ('WT/TR', 'Wartorn/Trade')])