from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    description =  models.TextField()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField() 
    price = models.FloatField() 
    created_at = models.DateField()
    manufacture = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.price}, {self.created_at}'
      
