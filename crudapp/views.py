from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import student

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll = request.POST['roll']
        age = request.POST['age']
        email = request.POST['email']
        mbl = request.POST['mbl']
        add = request.POST['add']
        student.objects.create(name=name, roll=roll, age=age, email=email, mbl=mbl, add=add)
        data = student.objects.all()
        return render(request, 'read.html', {'data':data})
    
    return render(request, 'index.html')  

def read(request):
    data = student.objects.all()
    return render(request, 'read.html', {'data':data})

def update(request, id):
    data = get_object_or_404(student, id=id)
    if request.method == 'POST':
        data.name = request.POST['name']
        data.roll = request.POST['roll']
        data.age = request.POST['age']
        data.email = request.POST['email']
        data.mbl = request.POST['mbl']
        data.add = request.POST['add']
        data.save()
        return redirect('read')
    return render(request, 'update.html', {'data':data})

def delete(request, id):
    data = student.objects.get( id=id)
    data.delete()
    return redirect('read')