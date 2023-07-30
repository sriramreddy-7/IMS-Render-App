from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,logout,login
from django.db.models import Count
from django.contrib.auth.models import User
from student.models import Jobs,Std,SD2,btech_25
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'login.html')


def home(request):
    return render(request,'home.html')


def my_login(request):
    if request.method =='POST':
            print("Post Requested Recevied!")
            designation = request.POST['designation']
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if designation == 'student' :
                    return redirect('student_dashboard')
                elif designation == 'tpo' and username=="tpo":
                    return redirect('tpo_dashboard')
                else:
                    return HttpResponse('<h1 style="color:blue;"> Login Sucessful to Admin dashbaord </h1>')
            else:
                return render(request,'login.html')
    else:            
        return render(request,'login.html')
    
@login_required    
def tpo_dashboard(request):
    student_counts = Std.objects.values('branch', 'section').annotate(total_students=Count('hall_ticket_no'))
    context = {
        'student_counts': student_counts,
    }
    return render(request,'tpo_dashboard.html',context)

@login_required    
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
        jobs=Jobs.objects.all()
        return render(request,'job_listing.html',{'jobs':jobs})
    else:
        return render(request,'tpo_post_job.html')

@login_required       
def student_dashboard(request):
    
    jobs=Jobs.objects.all()
    return render(request,'student_dashboard.html',{'jobs':jobs})


def data_store(request):
    return HttpResponse('<h1 style="color:green;"> Details has been stored succesfully into the database !</h1>')

@login_required    
def all_students(request):
    std=Std.objects.all()
    return render(request,'all_students.html',{'std':std})
@login_required    
def sd2(request):
    std=SD2.objects.all()
    return render(request,'sd2.html',{'std':std})

@cache_control(no_cache=True, must_revalidate=True)
def logout_view(request):
    logout(request)
    response = HttpResponseRedirect('/')
    response.delete_cookie('sessionid')
    return response
  
    
def info(request):
    return render(request,'info.html')

@login_required    
def all(request):
    std=Std.objects.all()
    return render(request,'all.html',{'std':std})

@login_required    
def job_listing(request):
    jobs=Jobs.objects.all()
    return render(request,'job_listing.html',{'jobs':jobs})

@login_required    
def all_btech_25(request):
    std=btech_25.objects.all()
    return render(request,'btech_25.html',{'std':std})


@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        if request.user.check_password(current_password):
            if new_password == confirm_new_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)

                messages.success(request, 'Password successfully changed.')
                return redirect('logout_view') 
            else:
                messages.error(request, 'New passwords do not match.')
        else:
            messages.error(request, 'Current password is incorrect.')

    return render(request, 'change_password.html')

