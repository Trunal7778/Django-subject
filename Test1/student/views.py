
from collections import OrderedDict

from django.shortcuts import get_object_or_404, redirect, render

from.models import Attendance, Course, Student 

from .forms import StudentForm 

from .forms import CourseForm

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy 

#from django.http import HttpResponse
# Create your views here.

#def home(request):
#return HttpResponse("Hello, Trunal prajapati welcome to django world !")  

def home(request): 
    data = {
     'name': 'Trunal Prajapati',
     'course': 'Django',
     'collage': 'JG UNIVERSITY' 
    } 
    subject = ['python','Django','agile','angular', 'Big data']
    return render(request, 'index.html',{'data': data, 'subject': subject, 'Marks': 80})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'About.html') 

def studentList(request): 
    students = Student.objects.all()
    return render(request, 'student_crud/list.html', {'students': students})

def student_edit(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name', '').strip()
        student.email = request.POST.get('email', '').strip()
        student.mobile = request.POST.get('mobile', '').strip()
        student.save()
        return redirect('studentList')

    return render(request, 'student_crud/edit.html', {'student': student})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('studentList')  

def attendance_list(request):
    attendance_records = Attendance.objects.select_related('student').order_by('date', 'student__name')
    grouped_records = OrderedDict()

    for record in attendance_records:
        grouped_records.setdefault(record.date, []).append(record)

    return render(request, 'student_crud/attendencelist.html', {'attendance_by_date': grouped_records.items()}) 

# def add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '').strip()
#         email = request.POST.get('email', '').strip()
#         mobile = request.POST.get('mobile', '').strip()
       

#         student = Student.objects.create(
#             name=name,
#             email=email,
#             mobile=mobile,
#         )
#         return redirect('studentList')

#     return render(request, 'student_crud/add.html', {}) 

def student_add(request):
    if request.method == 'POST':
         form = StudentForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('studentList')
    else:
        form = StudentForm()
    return render(request, 'student_crud/add.html', {'form': form})


def add_attendance(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        date = request.POST.get('date')
        status = request.POST.get('status')

        student = get_object_or_404(Student, id=student_id)

        attendance = Attendance.objects.create(
            student=student,
            date=date,
            status=status,
        )
        return redirect('attendance_list')


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_crud/courseform.html'
    success_url = reverse_lazy('course_list')

class CourseListView(ListView):
    model = Course
    template_name = 'course_crud/course_list.html'
    context_object_name = 'courses'
    queryset = Course.objects.all().order_by('-id')
    success_url = reverse_lazy('course_list')