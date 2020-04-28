# polls/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic      # !!!

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """최근 게시된 투표 5개 반환"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=int(request.POST['choice']))
    except (KeyError, Choice.DoesNotExist):
        # 투표 양식을 다시 출력
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "투표 항목을 선택하지 않았습니다.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터 처리가 성공하면, 항상 HttpResponseRedirect를 반환하라.
        # 이렇게 해야, 사용자가 돌아가기 버튼을 클릭해도 두번 게시되는 현상을 방지할 수 있다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
