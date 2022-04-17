from django.db import models
from shop.models import catag,products

# Create your models here.
class cartlist(models.Model):
    car_id=models.CharField(max_length=250,unique=True)
    dat_added=models.DateField(auto_now=True)
    def __str__(self):
        return self.car_id
class items(models.Model):
    prod=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    qnty=models.IntegerField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.prod
    def total(self):
        return self.prod.price*self.qnty