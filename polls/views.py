from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)

def results(request, question_id):
    return HttpResponse(f"You are looking at question {question_id} RESULTS")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question': question})
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    # return render(request, 'polls/index.html', {'question': question})

def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id} VOTE")

# Create your views here.