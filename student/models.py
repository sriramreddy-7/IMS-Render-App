from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Jobs(models.Model):
    job_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    job_type = models.CharField(max_length=100)
    job_url = models.URLField()
    post_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField()

    def __str__(self):
        return self.job_name
    
    
class Std(models.Model):
    hall_ticket_no = models.CharField(max_length=20, primary_key=True)
    student_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    email_id = models.EmailField(unique=True)

    def __str__(self):
        return self.hall_ticket_no
    
class SD2(models.Model):
    hall_ticket_no = models.CharField(max_length=20, primary_key=True)
    student_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    training_type = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    
    
class btech_25(models.Model):
    hall_ticket_no = models.CharField(max_length=20, primary_key=True)
    student_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    
# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class User(AbstractUser):
#     # Fields for students
#     hall_ticket_no = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     dept_or_branch = models.CharField(max_length=100)
#     year_of_study = models.IntegerField()
#     passout_year = models.IntegerField()
#     profile_photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)
#     clg_email = models.EmailField(max_length=254, unique=True)
#     personal_email =models.EmailField(max_length=254, unique=True)
#     mobile_number=models.CharField(max_length=10, unique=True)
#     linked_url = models.URLField(max_length=255)
#     github_url = models.URLField(max_length=255)
#     twitter_url = models.URLField(max_length=255)
#     instagram_url = models.URLField(max_length=255)
#     resume = models.FileField(upload_to='resumes', blank=True, null=True)
   
#     # Fields for faculty
#     mobile_no = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     user_type = models.CharField(max_length=100, choices=[('student', 'Student'), ('faculty', 'Faculty')], default='student')
#     login_time = models.DateTimeField(auto_now_add=True)
#     logout_time = models.DateTimeField(null=True, blank=True)
#     ip_address = models.GenericIPAddressField()

#     class Meta:
#         db_table = 'user'

#     def __str__(self):
#         return self.email 
class pe_se(models.Model):
    hallticket_no = models.CharField(max_length=12,primary_key=True)
    student_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    Year_Sem_Branch_Spl_Sec=models.CharField(max_length=50) 
    faculty_Name=models.CharField(max_length=50) 
    elective=models.CharField(max_length=50) 
