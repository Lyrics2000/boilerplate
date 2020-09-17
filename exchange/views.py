from django.shortcuts import render
from .creadentials import RequestCalculations

# Create your views here.
def exchange_dark(request):
    object = RequestCalculations.x
    print(object.text)
    return render(request,'exchange-dark.html',{})
