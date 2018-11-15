"""school_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from school_app.views import IndexView,SchoolRegView,SchoolListView,StudentListView,SchoolDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school_app/', include('school_app.urls')),
    path('', IndexView.as_view(), name="index"),
    path('schools/', SchoolListView.as_view(), name="schools"),
    path('students/', StudentListView.as_view(), name="students"),
    #path('school_detail/', SchoolDetailView.as_view(), name="school-detail"),
    path('schoolreg/', SchoolRegView.as_view(), name="schoolreg"),
]
