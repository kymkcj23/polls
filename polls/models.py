# polls/models.py
from django.db import models
from django.utils import timezone   # 추가
import datetime                     # 추가


class Question(models.Model):
    question_text = models.CharField('질문 문구', max_length=200)
    pub_date = models.DateTimeField('게시 일자')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'       # 추가
    was_published_recently.boolean = True                       # 추가
    was_published_recently.short_description = '최근 게시?'      # 추가


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text