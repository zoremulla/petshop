from django.db import models

# Create your models here.
class pets(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    available = models.BooleanField(null=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=3)