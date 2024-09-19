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
    if request.method == 'POST':
        openai.api_key = settings.OPENAI_API_KEY
        responses = request.POST.get('responses')
        responses_data = json.loads(responses)
        prompt = f'''create a responsive website using html, css and js, put it in a single html file, Use fontawsome for icons, make the best design and animations possible. Just give the code, no explanations or summary please. where ever image is required use the alt as "Image Here". Don't use markdown for the code, just give the raw text. The exact requirements are given in the following json: {responses_data}'''

        print(responses_data)

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        print(source_code)

        source_code = response.choices[0].message.content.strip()
        with open(os.path.join(settings.BASE_DIR, 'webGenerator', 'generated_source_code.txt'), 'w') as file:
            file.write(source_code)

        return JsonResponse({'success': True})
    else:
        return render(request, 'webGenerator.html')

@csrf_exempt
@login_required
def preview (request):
    try:
        with open(os.path.join(settings.BASE_DIR, 'webGenerator', 'generated_source_code.txt'), 'r') as file:
            source_code = file.read()
    except FileNotFoundError:
        source_code = '<h1>Something went wrong :(</h1>'
    
    return render(request, 'preview.html', {'source_code': source_code})





# THE PROMPT: create a responsive website using html, css and js, put it in a single html file, Use fontawsome for icons, make the best design and animations possible. Just give the code, no explanations or summary please. where ever image is required use the alt as "Image Here". Don't use markdown for the code, just give the raw text. The exact requirements are given in the following json