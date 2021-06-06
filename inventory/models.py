import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
	code = models.IntegerField()
	name = models.CharField(max_length=255)
	options = (
			(1, 'Female'),
			(2, 'Male'),
			(3, 'Kids'),
			(4, 'Bedroom'),
			(5, 'Kitchen'),
			(6, 'Bathroom'),
		)
	option = models.CharField(max_length=255, default='', choices=options)
	registered_at = models.DateTimeField()

	def __str__(self):
		return self.name


class Brand(models.Model):
	name = models.CharField(max_length=255)
	group_level_prices = (
				 (1, 'Low'),
				 (2, 'Middle'),
				 (3, 'High'),
			)
	level_price = models.CharField(max_length=1, default='', choices=group_level_prices)
	registered_at = models.DateTimeField()

	def __str__(self):
		return self.name


class Product(models.Model):
	sku = models.CharField(max_length=255, default='')
	name = models.CharField(max_length=255)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE) 
	
	group_sizes = (
			('S','Short'),
			('M','Medium'),
			('L','Large'),
		)
	size = models.CharField(max_length=1, choices=group_sizes)

	quantity = models.IntegerField()
	unit_price = models.DecimalField(max_digits=10, decimal_places=2)	
	registered_by = models.CharField(max_length=255)
	registered_at = models.DateTimeField()
	modified_by = models.CharField(max_length=255)
	modified_at = models.DateTimeField()
	is_active = models.BooleanField()
	
	def __str__(self):
		return self.name
