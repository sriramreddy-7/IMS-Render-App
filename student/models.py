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