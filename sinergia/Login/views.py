
from django.shortcuts import render


# Create your views here.
def helloWorld(request):
    return render(request,'index.html')

def LoginPage(request):
    return redner(request,'Pages/Login.html')
