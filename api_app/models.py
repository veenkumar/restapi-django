import email
from pyexpat import model
from django.db import models


class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()


class SendYourQueries(models.Model):
    service_type = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    your_queries = models.CharField(max_length=200)

