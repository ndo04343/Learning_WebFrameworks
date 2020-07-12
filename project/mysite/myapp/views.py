from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.

def index(request):
    return render(request, 'myapp/home.html')

def index_question(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'myapp/questions.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'myapp/question_detail.html', context)