from django.shortcuts import render

# Create your views here.
def exchange_dark(request):
    return render(request,'exchange-dark.html',{})
