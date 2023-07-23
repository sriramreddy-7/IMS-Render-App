from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from django.contrib.auth.models import User
from student.models import Jobs
# Create your views here.
def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')


def my_login(request):
    if request.method =='POST':
            designation = request.POST['designation']
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if designation == 'student' :
                    return redirect('student_dashboard')
                    # j=Jobs.objects.all()
                    # return render(request,'student_dashboard.html',{'j':j})
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
        deadline_date=request.POST.get('deadline_date')
        print(company_name)
        print(job_name)
        print(job_type)
        print(job_url)
        context = {
            'job_name': job_name,
            'company_name': company_name,
            'job_type': job_type,
            'job_url': job_url,
            'deadline_date':deadline_date,
        }
        job=Jobs.objects.create(job_name=job_name,company_name=company_name,job_type=job_type,job_url=job_url,deadline_date=deadline_date)
        job.save()
        j=Jobs.objects.all()
        return render(request,'student_dashboard.html',{'j':j})
    else:
        return render(request,'tpo_post_job.html')
    
def student_dashboard(request):
    j=Jobs.objects.all()
    return render(request,'student_dashboard.html',{'j':j})