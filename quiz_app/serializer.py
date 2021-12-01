from .models import Quiz
from rest_framework import serializers


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Quiz
        fields = ("Question","op1","op2","op3","op4","Answer")
