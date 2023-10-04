from django.shortcuts import render
from .models import employee
# Create your views here.
def detail(request):
    res = employee.objects.all()
    return render(request,"read.html",{'employees':res})
