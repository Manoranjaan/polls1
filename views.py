from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.views import generic
# Create your views here.
def index(request):
    latest_question = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question}
    return render(request, 'polls/index.html', context)


def details(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/details.html',{'question':question})


def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/result.html',{'question':question})

def votes(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        sleceted_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/details.html',{"question":question},{'error':'you didnt select a choice waste fellow'})
    else:
        sleceted_choice.votes += 1
        sleceted_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
