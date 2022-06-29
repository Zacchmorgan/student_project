from dataclasses import fields
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('fullname','mobile','csuid','course')
        labels = {
            'fullname':'Full Name',
            'csuid':'CSU. ID'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['course'].empty_label = "Select Course"