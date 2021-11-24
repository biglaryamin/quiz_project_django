from django.shortcuts import render
from .models import Quiz


def test_view(request):
    all_quiz=Quiz.objects.all()
    return render(request,"test.html",{"all_quiz":all_quiz})



def detail_view(request,id):
    the_quiz=Quiz.objects.get(id=id)
    return render(request,"detail.html",{"the_quiz":the_quiz})




# def vote(request):
#     return render()