from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from .models import User


def index(request):
    context= {
    'users': User.objects.all()
    }
    return render(request, 'users/index.html', context)


def new(request):
    return render(request, 'users/create.html')

def create(request):
    print(request.POST)
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect ('users/new')
    else:
            User.objects.create(fullname = request.POST['fullname'], email = request.POST['email'])
    return redirect('/users')

def show(request, number):
    context = {
    "user" : User.objects.get(id=(number))
    }
    return render(request, "users/show.html", context)

def edit(request, number):
    context = {
    "user" : User.objects.get(id=(number))}
    return render(request, "users/edit.html", context)

def update(request, number):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        user = User.objects.get(id=(number))
        user.fullname = request.POST['fullname']
        user.email = request.POST['email']
        user.save()
    return redirect('/')

def delete(request, number):
	user = User.objects.get(id=(number))
	user.delete()
	return redirect('/users')
