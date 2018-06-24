from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Inventory(models.Model):
    inventory_type = models.CharField(max_length=50)
    #number = models.IntegerField(max_length=10)
    #material = models.CharField(max_length=20)
    date_add = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = '库存类别'
    def __str__(self):
        return self.inventory_type

class Element(models.Model):
    type = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    material = models.CharField(max_length=20)
    bianhao = models.CharField(max_length=30)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '详细库存'

    def __str__(self):
        return self.name


