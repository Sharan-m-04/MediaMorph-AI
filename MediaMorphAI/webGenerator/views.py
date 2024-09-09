from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from openai import OpenAI
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@csrf_exempt
@login_required
def generateweb(request):
    return render(request, 'webGenerator.html')