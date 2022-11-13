from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

from app.models import User


# Create views

def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
    }
    return render(request, 'index.html', tparams)


# def authorins(request):
#     if not request.user.is_authoricated or request.user.username != 'admin':
#         return redirect('/login')
#     # if POST request, process from data
#     if request.method == 'POST':
#         # create form instance and pass data to it
#         form = UserInsForm(request.POST)
#         if form.is_valid(): # is it valid?
#             username = form.cleaned_data['email']
#             email = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             a = User(email=email, username=username, password=username)
#             a.save()
#             return HttpResponse("<h1>Author Inserted!<h1>")
#     # if GET (or any other method), create black form
#     else:
#         form = UserInsForm()
#     return render(request, 'authorins.html', {'form':form})


def add_film(request):
    return None


def add_actor(request):
    return None


def add_director(request):
    return None


def edit_film(request):
    return None


def edit_actor(request):
    return None


def edit_director(request):
    return None


def delete_film(request):
    return None


def delete_actor(request):
    return None


def delete_director(request):
    return None