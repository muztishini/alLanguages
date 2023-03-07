from django.contrib import admin
from question_answer.models import Question, Answer
from my_user.models import User

admin.site.register(Question)
admin.site.register(Answer)
# admin.site.register(User)
