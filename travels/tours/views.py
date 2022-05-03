from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout

# Create your views here.


def index(request):
    return render(request,'tours/base.html')

def mylogin(req):
    if req.method=='GET':
        form=AuthenticationForm()
        context={'form':form}
        return render(req,'tours/login.html',context)

    elif req.method=='POST':
        form=AuthenticationForm(req.POST)
        username=req.POST['username']
        password=req.POST['password']
        user=authenticate(req,username=username,password=password)
        if user:
            login(req,user)
            return redirect('Home')
    else:
        context={'form':form}
        return render(req,'tours/login.html',context)
def mylogout(req):
     logout(req)
     return redirect('Home')
from .forms import MyUserCreationForm   
def myregister(req):
    if req.method=='POST':
        form=MyUserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=MyUserCreationForm()
        context={'form':form}
        return render(req,'tours/register.html',context)
