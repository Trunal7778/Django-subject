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