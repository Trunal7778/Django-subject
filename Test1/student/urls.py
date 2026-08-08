from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'), 
    path('studentList/', views.studentList, name='studentList'), 
    path('add/', views.student_add, name='add'), 
    path('student/edit/<int:id>/', views.student_edit, name='student_edit'),
    path('student/delete/<int:id>/', views.student_delete, name='student_delete') ,
    path('attendance/', views.attendance_list, name='attendance_list'),
   
    #cbv for course
    path('course/list/', views.CourseListView.as_view(), name='course_list'),
    path('course/add/', views.CourseCreateView.as_view(), name='course_add'),
] 

