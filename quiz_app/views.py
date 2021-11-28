from typing import List
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Quiz


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