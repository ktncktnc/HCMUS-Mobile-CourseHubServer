from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Syllabus
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.forms.models import model_to_dict
import json


# Create your views here.
def index(request):
    return HttpResponse("Hey, what quizes are you looking for?")

def get_syllabus(request, syllabus_id):
    syllabus = model_to_dict(get_object_or_404(Syllabus, pk = syllabus_id))
    if not syllabus:
        return JsonResponse({})
    return JsonResponse(syllabus)
