from django.shortcuts import render
from .forms import ingreboleta
from .models import ingresoboleta 

# Create your views here.
def inicioingresoboleta(request):
	form = ingreboleta(request.POST or None)

	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get("numerodeboleta1")
		# obj = ingresoboleta.objects.Create(numerodeboleta=abc)
		obj2 = ingresoboleta()
		obj2.numerodeboleta=abc
		obj2.save()

	return render(request,"inicioingresoboletas.html", {'form':form})