from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=128)
    description=models.TextField()
    price=models.IntegerField()
    supplier=models.CharField(max_length=64)
    buy_count=models.IntegerField()

    def __str__(self):
        return self.name
