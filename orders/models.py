import datetime
from django.db import models
from django.utils import timezone
from inventory.models import Product

# Create your models here.
class Order(models.Model):
	cpf = models.CharField(max_length=12)
	name = models.CharField(max_length=255)
	phone = models.CharField(max_length=255, default='')
	products = models.ManyToManyField(Product)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	registered_at = models.DateTimeField()
	registered_by = models.CharField(max_length=255)

	def searchProduct(self):
		pass

	def setOrderQuantityProduct(self):
		quantity_per_product = [len(self.products.all())]
		qtd_products = len(self.products.all())
		query_products = self.products.all()
		quantity = 10
		index = 0
		index2 = 0
		local_price = 0.00

		while index < len(self.products.all()):
			print("index ", index)
			print("product ", query_products[index])
			print(str({quantity, query_products[index].name}))
			quantity_per_product[index] = {quantity, query_products[index].price}
			#quantity_per_product[index] += query_products[index].name

			print('end')
			print(len(quantity_per_product))
			print(quantity_per_product)
			print(quantity_per_product[0])
			
			quantity_per_product = list(quantity_per_product[0])
			print(quantity_per_product[0])
			print(quantity_per_product[1])

			local_price = local_price + (quantity_per_product[0] * float(quantity_per_product[1]))

			print(local_price)

			index = index + 1


		#b = a[0] * a[1]
		#print(b)

	def setOrderPrice(self):
		try:
			qtd = len(self.products.all())
			print(qtd)
		except Exception as e:
			raise e

	def updateQuantityProduct(self):
		pass