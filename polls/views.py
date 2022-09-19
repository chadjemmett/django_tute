from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world Youre at the polls index")

def results(request, question_id):
    return HttpResponse(f"You are looking at question {question_id}")

def detail(request, question_id):
    return HttpResponse(f"You are looking at question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")

# Create your views here.
