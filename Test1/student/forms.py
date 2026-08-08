from django import forms
from .models import Course, Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__" 

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'}),
        }