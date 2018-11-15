from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,UpdateView
from school_app.models import School, Student
from school_app.forms import SchoolForm, StudentForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolRegView(TemplateView):
    template_name = 'schoolreg.html'
    

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School 
    template_name = 'schools.html'
    fields = ('name', 'school_id_num', 'principal', 'location')
    
    
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'school-detail.html'


class SchoolUpdateView(UpdateView):
    model = School
    form_class = SchoolForm
    template_name = 'school_update_form.html'
    
    
class StudentListView(ListView):
    context_object_name = 'students'
    model = Student
    template_name = 'students.html'
    fields = ('name', 'dob', 'school')
