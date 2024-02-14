from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
