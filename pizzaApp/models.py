from django.db import models

# Create your models here. # create a model when you need a database
# whenever you create a model, it creates a database

class PizzaModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    

class CustomerModel(models.Model):
    userid = models.CharField(max_length=50)  # inbuilt id provided by django
    phoneno = models.CharField(max_length=50)


class OrderModel(models.Model):
    username = models.CharField(max_length=50) 
    phoneno = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    ordereditems = models.CharField(max_length=50)
    status = models.CharField(max_length=50)