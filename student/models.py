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
    
    