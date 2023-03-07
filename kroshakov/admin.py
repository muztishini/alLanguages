from django.contrib import admin
from kroshakov.models import Question, Answer, Users

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Users)
