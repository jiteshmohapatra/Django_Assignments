from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
def fn6(request):
    send_mail(
        "CMS ALERT",
        "Greetings from edunet foundation 3000 has been credited your account",
        "jiteshmohapatra2000@gmail.com",
        ["mohapatraraja200@gmail.com","sayan12842@gmail.com","agrawal.subhashree@gmail.com","avijitdutta8798@gmail.com"],
        fail_silently=False,
)
 
    return HttpResponse("welcome Mail transfer Protocol")

# Create your views here.
