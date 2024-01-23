# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .forms import UserDetail
from .models import User

def index(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserDetail(request.POST)
        if form.is_valid():
            form.save()
            form = UserDetail()
        else:
            print("Form is not valid. Errors:", form.errors)
    else:
        form = UserDetail()

    return render(request, 'user/index.html', {'form': form, 'users': users})

def updateuser(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        fm = UserDetail(request.POST, instance=user)
        if fm.is_valid():
            fm.save()
            return redirect('index') 
    else:
        fm = UserDetail(instance=user)
    return render(request, 'user/updateuser.html', {'form': fm})

def deleteuser(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('index')
    else:
        return render(request, 'user/index.html', {'form': UserDetail(), 'users': User.objects.all()})
