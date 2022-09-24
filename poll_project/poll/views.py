from multiprocessing import context
from django.shortcuts import render
from .forms import create_poll_form
from .models import poll

def home(request):
    context={}
    return render(request, 'poll/home.html', context)

def create(request):
    form = create_poll_form()
    context={ 'form': form }
    return render(request, 'poll/create.html', context)

def vote(request, poll_id):
    context={}
    return render(request, 'poll/vote.html', context)

def results(request, poll_id):
    context={}
    return render(request, 'poll/results.html', context)

