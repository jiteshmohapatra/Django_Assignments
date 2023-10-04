from django.shortcuts import render
from django.http import HttpResponse
def fn1(request):
    #return HttpResponse("<h2 style=color:green;>welcome to the django frame work")
    return render(request,"index.html")

def fn2(request):
    #return HttpResponse("<h2 style=color:Blue;>Welcome to the django project here it is the My 1st View Creation")
    return render(request,"portfolio.html")

# Create your views here.
