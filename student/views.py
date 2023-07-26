from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from django.contrib.auth.models import User
from student.models import Jobs,Std,SD2
import pandas as pd
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


def data_store(request):
    # csv_file_path = r"C:\Users\sriramreddykoonadi\Project\IMS\IMS\CSE_25_DB.csv"
    csv_file_path = r"C:\Users\sriramreddykoonadi\Downloads\SD-2_EZ.csv"
    df = pd.read_csv(csv_file_path)
    print(df.columns)
    print(df.dtypes)

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
        hall_ticket_no = row['Roll No']
        student_name = row['Student Name']
        branch = row['Branch']
        section = row['SD-2']
        email_id = row['Email']
        venue=row['Venue']

        # Adjust and format the data as needed
        student_name = student_name.title().strip()  # Capitalize student name and remove leading/trailing spaces
        branch = branch.strip()
        hall_ticket_no=hall_ticket_no.strip()
        section=section.strip()
        email_id=email_id.strip()
        venue=venue.strip()
        print(hall_ticket_no)
        obj = SD2(
            hall_ticket_no=hall_ticket_no,
            student_name=student_name,
            branch=branch,
            training_type=section,
            venue=venue,
            email_id=email_id,
        )
        obj.save()
        
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