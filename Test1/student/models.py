from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
   
    email = models.EmailField()
    
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name  
    
class Course(models.Model):
    
    courseName = models.CharField(max_length=100)
    courseCode=models.CharField(max_length=50)
    startDate=models.DateField()
    endDate=models.DateField()
    facultyName=models.CharField(max_length=100)
    isActive=models.BooleanField(default=True)
    
    def __str__(self):
        return self.courseName 

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ] 
    student = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )
    remarks = models.CharField(
        max_length=100,
        blank=True, 
        null=True
    )
    def __str__(self):
        return f"{self.student} - {self.date}"
