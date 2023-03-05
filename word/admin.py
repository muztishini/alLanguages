from django.contrib import admin
from word.models import Word, WordTranslate, Progress


admin.site.register(Word)
admin.site.register(WordTranslate)
admin.site.register(Progress)

