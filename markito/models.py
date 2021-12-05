from django.db import models
from accounts.models import CustomUser


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return  self.name


class Products(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    count = models.PositiveIntegerField(default=0)
    buy_price = models.DecimalField(max_digits=50, decimal_places=2)
    sell_price = models.DecimalField(max_digits=50, decimal_places=2)
    side_costs = models.DecimalField(max_digits=50, decimal_places=2)
    costs = models.DecimalField(max_digits=50, decimal_places=2)
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name



