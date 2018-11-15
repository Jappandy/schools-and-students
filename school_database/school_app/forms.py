from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from school_app.models import School, Student

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('name', 'school_id_num', 'principal', 'location')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save School'))
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'dob', 'school')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Student'))
        
        
    