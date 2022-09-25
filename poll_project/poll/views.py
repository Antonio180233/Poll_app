from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import create_poll_form
from .models import poll

def home(request):
    polls=poll.objects.all()
    context={'polls': polls}
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method=='POST':
        form=create_poll_form(request.POST)
        if form.is_valid():
            form.save()
            return   redirect('home')
    else: form=create_poll_form()
           
    context={ 'form': form }
    return render(request, 'poll/create.html', context)

def vote(request, poll_id):
  
    Poll= poll.objects.get(pk=poll_id)
    if request.method=='POST':
        selected_option= request.POST['poll']
        if selected_option=='option1':
            Poll.option_one_count+=1
        elif selected_option=='option2':
            Poll.option_two_count+=1
        elif selected_option=='option3':
            Poll.option_three_count+=1
        else:
            return HttpResponse(400, 'Invalid form')
        Poll.save()
        return redirect('results', poll_id)

    context={
        'poll': Poll

    }
    return render(request, 'poll/vote.html', context)

def results(request, poll_id):
    Poll=poll.objects.get(pk=poll_id)
    context={
        'poll': Poll
    }
    return render(request, 'poll/results.html', context)


   

