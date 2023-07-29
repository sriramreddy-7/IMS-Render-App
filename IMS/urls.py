"""
URL configuration for IMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('sru',views.index,name="sru"),
    path('login',views.my_login,name="login"),
    path('home',views.home,name="home"),
    path('tpo_dashboard',views.tpo_dashboard,name="tpo_dashboard"),
    path('tpo_post_job',views.tpo_post_job,name="tpo_post_job"),
    path('student_dashboard',views.student_dashboard,name="student_dashboard"),
    path('data_store',views.data_store,name="data_store"),
    path('all_students',views.all_students,name="all_students"),
    path('sd2',views.sd2,name="sd2"),
    path('logout_view',views.logout_view,name="logout_view"),
    path('info',views.info,name="info"),
]
