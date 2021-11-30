from typing import List
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Quiz
from .forms import QuizForm

def home_view(request):
    return render(request,"homepage.html")


def list_view(request):
    all_quiz=Quiz.objects.all()
    return render(request,"list.html",{"all_quiz":all_quiz})


def detail_view(request,id):
    the_quiz    =Quiz.objects.get(id=id)
    right_answer=the_quiz.Answer
    return render(request,"detail.html",{"the_quiz"   :the_quiz,
                                        "right_answer":right_answer})


def add_vote(request):
    form=QuizForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request,"add_vote.html",{"form":form})  


# def save_form(request):
#     if request.method=='POST':
        
#         return render(request,"add_vote.html",{'form':form})


# from django.shortcuts import render
# from .forms import GeeksForm
  
# def home_view(request):
#     context ={}
  
#     # create object of form
#     form = GeeksForm(request.POST or None, request.FILES or None)
      
#     # check if form data is valid
#     if form.is_valid():
#         # save the form data to model
#         form.save()
  
#     context['form']= form
#     return render(request, "home.html", context)