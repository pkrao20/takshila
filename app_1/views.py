from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,HttpResponse
# from flask import current_app

from django.http import HttpResponse,HttpResponseRedirect
from app_1.models import data,contactus
import random


def home_function(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        comment=request.POST['comment']
        contactus(fname=fname,lname=lname,email=email,comment=comment).save()
        return render(request,'contact.html',{'msg':" We will connect you soon"})
    return render(request,'contact.html')

def quiz(request):
    return render(request,'quiz.html')

def register(request):
    if request.method=='POST':
        # is_private = request.POST.get('is_private', False);
        name=request.POST['name']
        qualification=request.POST['qualification']
        email=request.POST['email']
        password=request.POST['psw']
        repassword=request.POST['rpsw']
        c=request.POST['class']
        age=request.POST['age']
        if password != repassword:
            return render(request,'register.html',{'msg' :"please enter the same password"})
        data(name=name,qualification=qualification,email=email,password=password,c=c,age=age).save()
        return render(request, 'register.html',{'msg':"Registered successfully"})
        # (medicine_name=medicine_name,medicine_quantity=add,expiry_date=expiry_date).save() 
    return render(request,'register.html')




