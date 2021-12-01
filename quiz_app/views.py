from typing import List
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Quiz
from .forms import QuizForm
#For sign_up view
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
#For restfulApi
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import QuizSerializer


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



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




class QuizViewSet(viewsets.ModelViewSet):
    queryset         = Quiz.objects.all()
    serializer_class = QuizSerializer
