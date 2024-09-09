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






# THE PROMPT: create a responsive website using html, css and js, put it in a single html file, Use fontawsome for icons, make the best design and animations possible. Just give the code, no explanations or summary please. where ever image is required use the alt as "Image Here". Don't use markdown for the code, just give the raw text. The exact requirements are given in the following json