from django.db import models

# Create your models here.

class ProductInventory(models.Model):
	# Unique id is auto-created by django itself
	Name = models.CharField(max_length=100)
	Category = models.CharField(max_length=100)
	Price = models.FloatField()
	createdAt = models.DateTimeField(auto_now_add=True,null=True)
	updatedAt =  models.DateTimeField(auto_now=True,null=True)


