from django.shortcuts import render

from django.http import  JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from .models import newuser,Doctorinformation,uploadmedicine
# Create your views here.

def navbar(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_login(request):
    
    if request.method== 'POST':
        try:
            Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
            print("Username=",Userdetailes)
            request.session['Username']=Userdetailes.Username
            messages.success(request,"successfully login")
            return redirect('user_home')
        except newuser.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
    return render(request, 'user_login.html')

def user_registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if newuser.objects.filter(Username=Username).exists():
            messages.warning(request,'Username is already exists')
            return redirect('registration')
        else:
            newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
            messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
            return redirect('user_login')
    else:
        return render(request, 'user_registration.html')

def user_home(request):
    return render(request, 'userhome.html')



def user_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('navbar')


def admin_login(request):
    if request.method== 'POST':
        try:
            Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
            print("Username=",Userdetailes)
            request.session['Username']=Userdetailes.Username
            messages.success(request,"successfully login")
            return redirect('admin_home')
        except newuser.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
   
    return render(request, 'admin_login.html')

def admin_registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if newuser.objects.filter(Username=Username).exists():
            messages.warning(request,'Username is already exists')
            return redirect('admin_registration')
        else:
            newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
            messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
            return redirect('admin_login')
    else:
        return render(request, 'admin_registration.html')

def admin_home(request):
    return render(request, 'admin_home.html')


def admin_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('navbar')



def doctor_login(request):
    if request.method== 'POST':
        try:
            Userdetailes=Doctorinformation.objects.get(dname=request.POST['dname'], pass1=request.POST['pass1'])
            print("dname=",Userdetailes)
            request.session['dname']=Userdetailes.dname
            messages.success(request,"successfully login")
            return redirect('doctor_home')
        except Doctorinformation.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
   
    return render(request, 'doctor_login.html')

def doctor_registration(request):
    if request.method == 'POST':
        
        dname=request.POST['dname']
        address=request.POST['address']
        email=request.POST['email']
        mobileno=request.POST['mobileno']
        qual=request.POST['qual']
        exe=request.POST['exe']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if Doctorinformation.objects.filter(dname=dname).exists():
            messages.warning(request,'Username is already exists')
            return redirect('doctor_registration')
        else:
            Doctorinformation(dname=dname, address=address, email=email, mobileno=mobileno, qual=qual,exe=exe,pass1=pass1).save()
            messages.success(request, 'The new user '+request.POST['dname']+ " IS saved successfully..!")
            return redirect('doctor_login')
    else:
        return render(request, 'doctor_registration.html')

def doctor_home(request):
    return render(request, 'doctor_home.html')


def doctor_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('navbar')

def ngo_login(request):
    return render(request, 'ngo_login.html')

def ngo_registration(request):
    return render(request, 'ngo_registration.html')



def upload_medicine(request):
    if request.method == 'POST':
        tmedicine=request.POST['tmedicine']
        mname=request.POST['mname']
        cname=request.POST['cname']
        mdate=request.POST['mdate']
        exdate=request.POST['exdate']
        ml=request.POST['ml']
        medicine=request.POST['medicine']
        quantity=request.POST['quantity']
        uname=request.POST['uname']
        address=request.POST['address']
        phone=request.POST['phone']
        email=request.POST['email']
        image=request.FILES['image']
        image2=request.FILES['image2']
        uploadmedicine(tmedicine=tmedicine, mname=mname, cname=cname, mdate=mdate, exdate=exdate, ml=ml, medicine=medicine, quantity=quantity, uname=uname,address=address, phone=phone, email=email, image=image, image2=image2).save()
        messages.success(request, 'The new user '+request.POST['uname']+ " IS saved successfully..!")
        return redirect('user_home')
    else:
        return render(request, 'UploadMedicine.html')