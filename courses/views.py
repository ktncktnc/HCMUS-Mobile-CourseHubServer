from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Course
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.forms.models import model_to_dict
import json

def index(request):
    return HttpResponse("Hey, what are you looking for?")

def get_course(request, course_id):
    course = model_to_dict(get_object_or_404(Course, pk = course_id))
    if not course:
        return JsonResponse({})
    return JsonResponse(course)
