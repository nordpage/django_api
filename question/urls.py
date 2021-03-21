from django.conf.urls import url
from django.urls import path, re_path

from question.views import QuestionView, QuestionListView, QuestionKotlinView, QuestionJavaView, QuestionAndroidView

app_name = "questions"
urlpatterns = [
    path('questions/', QuestionListView.as_view()),
    path('questions/android/', QuestionAndroidView.as_view()),
    path('questions/java/', QuestionJavaView.as_view()),
    path('questions/kotlin/', QuestionKotlinView.as_view()),
]