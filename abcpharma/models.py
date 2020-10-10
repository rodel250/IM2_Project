from django.db import models
from datetime import datetime

# Create your models here.

class Person(models.Model):
        firstname = models.CharField(max_length = 50)
        middlename = models.CharField(max_length = 50)
        lastname = models.CharField(max_length = 50)
        address = models.CharField(max_length = 100)
        birthDate = models.DateField()
        birthPlace = models.CharField(max_length = 50)
        status = models.CharField(max_length = 10)
        gender = models.CharField(max_length = 10)
        spouseName = models.CharField(max_length = 50) 
        spouseOccupation = models.CharField(max_length = 20)
        children = models.IntegerField(default=0)
        motherName = models.CharField(max_length = 50)
        motherOccupation = models.CharField(max_length = 20)
        fatherName = models.CharField(max_length = 50)
        fatherOccupation = models.CharField(max_length = 20)
        height = models.FloatField()
        weight = models.FloatField()
        religion = models.CharField(max_length = 30)

        class Meta:
            db_table = "Person"

class Customer(Person):
    photo = models.FileField()
    dateRegistered = models.DateField(default = datetime.now())
    
    #option 1
    #medicines = models.ManyToManyField(Medicine)
    class Meta:
        db_table = "Customer"

class Medicine(models.Model):
    dateRegistered = models.DateField(default = datetime.now)
    SKU = models.AutoField(primary_key=True)
    category = models.CharField(max_length = 100)
    genericName = models.CharField(max_length = 100)
    commonBrand = models.CharField(max_length  = 100)
    manufacturedDate = models.DateField(default = datetime.now)
    expiryDate = models.DateField(default = datetime.now)
    size = models.IntegerField()
    howToUse = models.TextField()
    sideEffects = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    noOfItems = models.IntegerField()
    images = models.ImageField(upload_to='upload/')

    class Meta:
        db_table = "Medicine"

#option 2
class Order(models.Model):
  customer = models.ForeignKey(Customer, null = False, blank = False, on_delete = models.CASCADE, related_name = "Customer")
  medicine = models.ForeignKey(Medicine, null=False, blank = False, on_delete = models.CASCADE, related_name = "Medicine")
  orderedDate = models.DateField(default = datetime.now)
  quantity = models.IntegerField(default = 0)

  class Meta:
      db_table = "Order"