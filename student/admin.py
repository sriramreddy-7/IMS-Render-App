from django.contrib import admin
from student.models import Jobs,Std,SD2,btech_25
# Register your models here.
admin.site.register(Jobs)
admin.site.register(Std)
admin.site.register(SD2)
admin.site.register(btech_25)
# admin.site.register(User)

# from django.contrib import admin
# from .models import User


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'name', 'dept_or_branch', 'year_of_study', 'passout_year')
