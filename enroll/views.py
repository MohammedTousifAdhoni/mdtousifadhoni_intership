from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import StudentRegistration
from .models import User
from qrcode import *

# Create your views here.
def main(request):
    return render(request, 'enroll/main.html')

#adding and retrieving data
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/add.html', {'form':fm, 'stu':stud})

#edit and update function
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request,'enroll/update.html', {'form':fm})

#delete function

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def generate(request):
    return render(request, 'enroll/qr.html')

def qr(request):
    data = request.POST.get("data"
    )
    img = make(data)
    img.save('static/enroll/image/test.png')
    print(data)
    return redirect('/qrgenerator' ,{"data":data})