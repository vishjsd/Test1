from django.db import models

# Create your models here.
class ProductList(models.Model):
    SlNo=models.AutoField(primary_key=True)
    ProductName=models.CharField(max_length=100)
    ProductLowestPrice=models.CharField(max_length=10)
    LastUpdated=models.DateField(blank=True)


class ProductVariations(models.Model):
    id=models.AutoField(primary_key=True)
    Productid=models.CharField(max_length=100)
    VariationText=models.CharField(max_length=100)
    Stock=models.CharField(max_length=100)   
    LastUpdated=models.DateField(blank=True)



