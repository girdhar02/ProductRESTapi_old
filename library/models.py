from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100,blank=True)
    price=models.IntegerField( blank=True)
    image = models.ImageField(upload_to='Image')
    quantity=models.IntegerField(blank=True)
    
    def __str__(self):
        return self.name
