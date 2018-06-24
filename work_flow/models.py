from django.db import models

# Create your models here.
class Ele_Overview(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    material = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    flag = models.NullBooleanField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '零件概览'

    def __str__(self):
        return self.name

class Detial(models.Model):
    type = models.ForeignKey(Ele_Overview, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    flag = models.NullBooleanField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '详细工序'

    def __str__(self):
        return self.name