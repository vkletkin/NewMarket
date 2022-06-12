from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from products.models import Product


class Order(models.Model):
    amount = models.IntegerField()
    description=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    products=models.ManyToManyField(Product)