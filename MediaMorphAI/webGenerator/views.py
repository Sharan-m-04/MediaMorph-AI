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

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        source_code = response.choices[0].message.content.strip()
        request.session['source_code'] = source_code
        # return JsonResponse({'source_code': source_code})
        # print(f"Generated Source Code: {source_code}", flush=True)
        return redirect('preview.html')
    else:
        return render(request, 'webGenerator.html')

@csrf_exempt
@login_required
def preview (request):
    source_code = request.session.get('source_code', '')
    if not source_code:
        source_code = '<h1>Something went wrong :( <br> please try again later!</h1>'
    return render(request, 'preview.html', {'source_code': source_code})
    # return render(request, 'preview.html')





# THE PROMPT: create a responsive website using html, css and js, put it in a single html file, Use fontawsome for icons, make the best design and animations possible. Just give the code, no explanations or summary please. where ever image is required use the alt as "Image Here". Don't use markdown for the code, just give the raw text. The exact requirements are given in the following json