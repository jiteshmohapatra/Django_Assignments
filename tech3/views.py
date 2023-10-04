from django.shortcuts import render
from django.http import JsonResponse #It is a sub clas of http response means cjild class

def jsondata(request):
    data = [{'name':'john','country':'Germany'},{'name':'peter','country':'finland'},{'name':'jitesh mohapatra','age':24},{'name':'sk kumar','age':24,'city':'bhubaneswar'}]
    return JsonResponse(data,safe=False)
    

# Create your views here.
