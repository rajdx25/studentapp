from multiprocessing import context
from django.shortcuts import render,redirect
import studentapp
from studentapp.models import Student
from studentapp.forms import Form_view
from django.contrib import messages
from .forms import *
# Create your views here.


def index(request):
    return render(request,'studentapp/index.html')

def studentdetails(request):
    stu = Student.objects.all()
    return render(request,'studentapp/studentdetails.html', {'st':stu})


def adduser(request):
    
    if request.method=='POST':
        details= Form_view(request.POST)
       
        if details.is_valid():
            

            u_name = details.cleaned_data['studentname']
            u_address = details.cleaned_data['studentaddress']   
            u_email = details.cleaned_data['studentemail']
            u_number = details.cleaned_data['studentnumber']

            stu = Student(studentname=u_name, studentaddress = u_address, studentemail = u_email, 
                        studentnumber=u_number)

            stu.save()
            details = Form_view()
            
            
            messages.success(request,'employee added')
            return redirect('studentdetails')

    else:
            # messages.error(request,'employee not added')
        details = Form_view()
        
    return render(request,'studentapp/formhandling.html',{'form':details})

def delete(request,studentnumber):  
    record = Student.objects.get(studentnumber=studentnumber)
    context={}
    if request.method=='POST':

        record.delete()  
        return redirect("/")
    return render(request, "delete.html",context) 


# def formhandling(request):
#     form =Form_view()
#     return render(request,'studentapp/formhandling.html',{'form':form})