from django.db import models

# Create your models here.
class Offers(models.Model):
	name = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)

# class Products(models.Model):
# 	name = models.CharField(max_length=100)
# 	price = models.CharField(max_length=100)
# 	description = models.CharField(max_length=1000)
