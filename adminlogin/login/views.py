from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from login.models import Permission

# Create your views here.


def base(request):
    return render(request,'login/base.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=Permission.objects.get(username=username,password=password)

        if user is not None:
            return render(request,'login/base.html',{})
        else:
            print("someone tried to login and failed")
            print("They used username: {} and password: {}".format(username,password))
        return redirect('/')

    else:
        return render(request,'login/login.html')