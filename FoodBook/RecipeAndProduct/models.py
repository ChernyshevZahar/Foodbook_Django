from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=30,blank=True)
    price = models.DecimalField(default=0,max_digits=8,decimal_places=2)
    callorise = models.IntegerField(null=False, blank=True)
