from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,logout,login
from django.db.models import Count
from django.contrib.auth.models import User
from student.models import Jobs,Std,SD2,btech_25
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# import pandas as pd
# Create your views here.
def index(request):
    return render(request,'login.html')


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
                    return redirect('tpo_dashboard')
                else:
                    return HttpResponse('<h1 style="color:blue;"> Login Sucessful to Admin dashbaord </h1>')
            else:
                return render(request,'index.html')
    else:            
        return render(request,'index.html')
    
    
def tpo_dashboard(request):
    student_counts = Std.objects.values('branch', 'section').annotate(total_students=Count('hall_ticket_no'))
    context = {
        'student_counts': student_counts,
    }
    return render(request,'tpo_dashboard.html',context)

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
    
def student_dashboard(request):
    jobs=Jobs.objects.all()
    return render(request,'student_dashboard.html',{'jobs':jobs})


def data_store(request):
    # csv_file_path = r"C:\Users\sriramreddykoonadi\Project\IMS\IMS\CSE_25_DB.csv"
    # csv_file_path = r"C:\Users\sriramreddykoonadi\Downloads\SD-2_EZ.csv"
    # csv_file_path=r"C:\Users\sriramreddykoonadi\OneDrive - SR University\Bachelor of Technology\Database\References'\B.TECH_ALL_DEPTS_25(1).csv"
    # df = pd.read_csv(csv_file_path)
    # print(df.columns)
    # print(df.dtypes)
    # print(df.head())

    '''for index, row in df.iterrows():
        hall_ticket_no = row['HALLTICKET_NO']
        student_name = row['STUDENT_NAME']
        branch = row['BRANCH']
        section = row['SECTION']
        email_id = row['EMAIL_ID']

        # Adjust and format the data as needed
        student_name = student_name.title().strip()  # Capitalize student name and remove leading/trailing spaces
        branch = branch.strip()
        hall_ticket_no=hall_ticket_no.strip()
        section=section.strip()
        email_id=email_id.strip()
        
        obj = Std(
            hall_ticket_no=hall_ticket_no,
            student_name=student_name,
            branch=branch,
            section=section,
            email_id=email_id,
        )
        obj.save()'''
        
    '''for index, row in df.iterrows():
        obj = Std(
            hall_ticket_no=row['HALLTICKET_NO'],
            student_name=row['STUDENT_NAME'],
            branch=row['BRANCH '],  # Update to match the correct column name in your CSV file
            section=row['SECTION'],
            email_id=row['EMAIL_ID'],
        )
        obj.save()'''
    '''for index, row in df.iterrows():
        hall_ticket_no = row['H. T. No.']
        student_name = row['Name of the Student']
        branch = row['Dept.']
        
        # section = row['SD-2']
        email_id = row['Email Id']
        # venue=row['Venue']

        # Adjust and format the data as needed
        student_name = str(student_name).title().strip()  # Capitalize student name and remove leading/trailing spaces
        branch = str(branch).strip()
        hall_ticket_no=str(hall_ticket_no).strip()
        # section=section.strip()
        email_id=str(email_id).strip()
        # venue=venue.strip()
        
        obj = btech_25(
            hall_ticket_no=hall_ticket_no,
            student_name=student_name,
            branch=branch,
            # training_type=section,
            # venue=venue,
            email_id=email_id,
        )
        obj.save()
        print(f"{hall_ticket_no} Added to database!")'''
        
    # for index, row in df.iterrows():
    #     obj = Std(
    #         hall_ticket_no=row['HALLTICKET_NO'],
    #         student_name=row['STUDENT_NAME'],
    #         branch=row['BRANCH '],  # Update to match the correct column name in your CSV file
    #         section=row['SECTION'],
    #         email_id=row['EMAIL_ID'],
    #     )
    #     obj.save()   '''
    
    return HttpResponse('<h1 style="color:green;"> Details has been stored succesfully into the database !</h1>')

def all_students(request):
    std=Std.objects.all()
    return render(request,'all_students.html',{'std':std})

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

def all(request):
    std=Std.objects.all()
    return render(request,'all.html',{'std':std})


def job_listing(request):
    jobs=Jobs.objects.all()
    return render(request,'job_listing.html',{'jobs':jobs})


def all_btech_25(request):
    std=btech_25.objects.all()
    return render(request,'btech_25.html',{'std':std})