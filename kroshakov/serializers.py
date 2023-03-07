from rest_framework import serializers
from kroshakov.models import Question, Answer, Users


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
