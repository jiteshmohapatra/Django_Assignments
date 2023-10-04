from django.shortcuts import render
from .models import software
# Create your views here.
def salarydata(request):
    res = software.objects.all()
    return render(request,"software.html",{'softwares':res})