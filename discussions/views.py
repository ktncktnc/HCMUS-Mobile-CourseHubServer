from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Discussion
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.forms.models import model_to_dict
import json


# Create your views here.
def index(request):
    return HttpResponse("Hey, what discussions are you looking for?")

def get_discussion(request, discussion_id):
    discussion = model_to_dict(get_object_or_404(Discussion, pk = discussion_id))
    if not discussion:
        return JsonResponse({})
    return JsonResponse(discussion)
