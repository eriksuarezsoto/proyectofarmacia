from django.shortcuts import render
from django.template.loader import  get_template
from django.template import Context
from django.http  import HttpResponse,HttpResponseNotFound
import datetime

def horactual(request) :
    ahora=datetime.datetime.now()
    #t=get_template('horactual.html')
    html="<html><body>Dia y hora actual: %s.</body></html>" % ahora
   # if 404:
    #    return HttpResponseNotFound(html)
    # else:
      #  return HttpResponse('<h1>al nico le gusta el pikachu</h1>')


    return HttpResponse(html)