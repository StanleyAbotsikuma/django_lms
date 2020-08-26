"""trevillion_online_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
# development
from management.views import dev, index

#Teacher
from teacher.views import register,login,logout,dashboard,classroom,makelesson,profile,editlesson,students,messager

#Student
from student.views import register as studentRegistration,login as StudentLogin,logout, dashboard as studentDashboard,profile as StudentProfile, myClassroom as StudentClass,lessons

#notification

#messages

#templates
from django.views.generic import TemplateView

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('dev/' , dev),
    
    #teacher Access
    path('teacher/' , login),
    path('teacher/registration' , register),
    #teacher platform
    path('teacher/dashboard/' , dashboard),
    #profile
     path('teacher/profile/' , profile),
    #students
    path('teacher/students/' , students),
    #class links
    path('teacher/class/' ,classroom ),
    path('teacher/class/<room>/' ,classroom ),
    path('teacher/class/<room>/<subject_>/' ,classroom ),
    path('teacher/class/<room>/<subject_>/lesson/' ,makelesson),
    path('teacher/class/<room>/<subject_>/lesson/<int:lessonId>' ,editlesson),
    #messager
    path('teacher/messages/', messager),

    #logout
    path('logout/' ,logout  ),



    #Student Access
    path('student/' , StudentLogin),
    path('student/registration' , studentRegistration),
    #student Platform
    path('student/dashboard/', studentDashboard),
    # profile
    path('student/profile/',  StudentProfile),
    # My class
    path('student/myclass/',  StudentClass),
    #subjects
    path('student/myclass/<subject_>/' ,lessons),
    #notification
    #path('student/notification/' , notification),

    #notification
    #path('student/notification/' , notification),





    
]



urlpatterns += static(settings.STATIC_URL,	document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,	document_root = settings.MEDIA_ROOT)