from django.contrib import admin

# Register your models here.
from .models import ingresoboleta

class Adminingresoboleta(admin.ModelAdmin):
	list_display = ["__unicode__","numerodeboleta","fecha"]

	class meta:
		model = ingresoboleta

admin.site.register(ingresoboleta,Adminingresoboleta)

