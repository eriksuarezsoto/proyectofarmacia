from django.db import models
from django.contrib.auth.models import UserManager


# Create your models here.

class ingresoboleta(models.Model):
	codigo = models.IntegerField(default=1)
	nombre = models.CharField(max_length=50)
	fecha = models.DateTimeField(auto_now=False,auto_now_add=True)
	cantidad = models.IntegerField(default=1)
	precio = models.IntegerField(default=1)
	stock = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
	vendedor = models.IntegerField(default=1)
	numerodeboleta = models.IntegerField(default=1)
	factor = models.DecimalField(max_digits=3,decimal_places=2,default=1.5)
	conver = models.IntegerField(default=1)
	descuento = models.IntegerField(default=0)
	impresa = models.BooleanField(default=False)
	id = models.IntegerField(primary_key=True)
	def __unicode__(self):
		return self.codigo
