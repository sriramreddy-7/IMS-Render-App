from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.method=='POST':
        designation = request.POST['designation']
        user=authenticate(
        username=request.POST['username'],
        password=request.POST['password']
        )
        print(designation)
        # print(email)
        # print(password)
        if user is not None:
            login(request,user)
            return HttpResponse('<h1 style="color:green;"> Login Sucessful</h1>')
    else:
        return render(request,'index.html')

def home(request):
    return render(request,'home.html')