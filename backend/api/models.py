from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.IntegerField()