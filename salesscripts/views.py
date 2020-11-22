from django.shortcuts import render

def home(request):
    return render(request,'salesscripts/home.html')
