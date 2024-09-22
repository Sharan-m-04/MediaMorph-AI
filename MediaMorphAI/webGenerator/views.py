import os
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.conf import settings
from openai import OpenAI
import openai
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

@csrf_exempt
@login_required
def generateweb(request):
    return render(request, 'webGenerator.html')

@csrf_exempt
@login_required
def preview (request):
    if request.method == 'POST':
        openai.api_key = settings.SECRET_KEY
        responses = request.POST.get('responses')
        responses_data = json.loads(responses)
        prompt = f'''create a responsive website using html, css and js, put it in a single html file, Use fontawsome for icons, make the best design and animations possible. Just give the code, no explanations or summary please. where ever image is required use the alt as "Image Here". Don't use markdown for the code, just give the raw text. The exact requirements are given in the following json: {responses_data}'''

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2048,
        )

        source_code = response.choices[0].message.content.strip()

        down_file_path = os.path.join(settings.BASE_DIR, 'webGenerator', 'static', 'download', 'code.html')
        with open(down_file_path, 'w') as file:
            file.write(source_code)
    
        return render(request, 'preview.html', {'source_code': source_code})
    else:
        source_code = '<h1>Something went wrong :(</h1>'
        return render(request, 'preview.html', {'source_code': source_code})






# THE PROMPT: create a responsive website using html, css and js, put it in a single html file, Use fontawsome for icons, make the best design and animations possible. Just give the code, no explanations or summary please. where ever image is required use the alt as "Image Here". Don't use markdown for the code, just give the raw text. The exact requirements are given in the following json