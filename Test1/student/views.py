
from django.shortcuts import get_object_or_404, redirect, render

from.models import Student

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