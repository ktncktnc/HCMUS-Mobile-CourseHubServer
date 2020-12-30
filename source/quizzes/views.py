from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Quiz
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.forms.models import model_to_dict
import json
# Create your views here.

def index(request):
    return HttpResponse("What quiz are you looking for?")

def get_quiz(request, quiz_id):
    quiz = model_to_dict(get_object_or_404(Quiz, pk = quiz_id))
    if not quiz:
        return JsonResponse({})
    return JsonResponse(quiz)
