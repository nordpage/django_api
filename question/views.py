from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from .models import Question, Type
from .serializers import QuestionSerializer, QuestionListSerializer


class QuestionView(generics.CreateAPIView):
    seializer_class = QuestionSerializer

class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()

class QuestionAndroidView(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.filter(type__title='Android')

class QuestionJavaView(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.filter(type__title='Java')

class QuestionKotlinView(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.filter(type__title='Kotlin')

