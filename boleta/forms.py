from django import forms

class ingreboleta(forms.Form):
	codigo1 = forms.IntegerField()
	nombre1 = forms.CharField(max_length=50)
	fecha1 = forms.DateTimeField()
	cantidad1 = forms.IntegerField()
	precio1 = forms.IntegerField()
	stock1 = forms.IntegerField()
	total1 = forms.IntegerField()
	vendedor1 = forms.IntegerField()
	numerodeboleta1 = forms.IntegerField()
	factor1 = forms.DecimalField(max_digits=3,decimal_places=2)
	conver1 = forms.IntegerField()
	descuento1 = forms.IntegerField()
	impresa1 = forms.BooleanField()