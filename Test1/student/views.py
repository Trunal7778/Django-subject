# from urllib import request

from urllib import request

from django.shortcuts import render

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