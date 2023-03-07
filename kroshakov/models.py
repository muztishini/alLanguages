from django.db import models
from language.models import Language


class Users(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
