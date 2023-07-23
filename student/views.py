from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')


def my_login(request):
    if request.method=='POST':
            designation = request.POST['designation']
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if designation == 'student' :
                    return HttpResponse('<h1 style="color:green;"> Login Sucessful to Student dashbaord </h1>')
                elif designation == 'tpo' :
                    return render(request,'tpo_dashboard.html')
                else:
                    return HttpResponse('<h1 style="color:blue;"> Login Sucessful to Admin dashbaord </h1>')
            else:
                return render(request,'index.html')
    
    else:            
        return render(request,'index.html')
    
    
def tpo_dashboard(request):
    return render(request,'tpo_dashboard.html')

def tpo_post_job(request):
    if request.method == 'POST':
        job_name = request.POST['job_name']
        company_name=request.POST['company_name']
        job_type=request.POST['job_type']
        job_url=request.POST['job_url']
        print(company_name)
        print(job_name)
        print(job_type)
        print(job_url)
        context = {
            'job_name': job_name,
            'company_name': company_name,
            'job_type': job_type,
            'job_url': job_url,
        }
        return render(request,'student_dashboard.html',context)
    else:
        return render(request,'tpo_post_job.html')