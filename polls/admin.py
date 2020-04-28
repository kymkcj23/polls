from django.contrib import admin
from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3   # 선택 항목은 기본적으로 3개 준비


class QuestionAdmin(admin.ModelAdmin):      # `ModelAdmin`을 상속받는 클래스 생성
    fieldsets = [                           # 필드 순서 변경
        (None,        {'fields': ['question_text']}),
        ('날짜 정보', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']          # 추가
    search_fields = ['question_text']   # 추가


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)