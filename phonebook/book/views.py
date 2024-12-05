from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def Login(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
        else:
            messages.warning(req,'Invalid user name or password')
            return redirect(Login)
        # return redirect()
    else:
        return render(req,'login.html')

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['password']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
            return redirect(Login)
        except:
            messages.warning(req,'Email Already Exit')
            return redirect(register)
    else:
        return render(req,'register.html')
    