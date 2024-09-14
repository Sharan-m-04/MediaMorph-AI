from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.conf import settings
from openai import OpenAI
import openai
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

# @csrf_exempt
@login_required
def generateweb(request):
    if request.method == 'POST':
        openai.api_key = settings.OPENAI_API_KEY
        responses = request.POST.get('responses')
        responses_data = json.loads(responses)
        prompt = f'''create a responsive website using html, css and js, put it in a single html file, Use fontawsome for icons, make the best design and animations possible. Just give the code, no explanations or summary please. where ever image is required use the alt as "Image Here". Don't use markdown for the code, just give the raw text. The exact requirements are given in the following json: {responses_data}'''
        
        try:
            # response = openai.Completion.create(
            # model="text-davinci-003",
            # prompt=prompt,
            # max_tokens=2000
            # )
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[],
                temperature=1,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                response_format={
                    "type": "text"
                }
            )
            print(response)
            source_code = response.choices[0].message.content.strip()
            print(source_code)
            return redirect('preview.html')
        except Exception as e:
            print(f"Error with OpenAI API: {e}")
            return render(request, 'webGenerator.html', {'error': 'There was an error generating the website. Please try again.'})
    else:
        return render(request, 'webGenerator.html')


@login_required
def preview (request):
    # source_code = '''<html><head><style>body{color:red;}</style></head><body>This is working</body></html>'''
    source_code = source_code
    return render(request, 'preview.html', {'source_code': source_code})





# THE PROMPT: create a responsive website using html, css and js, put it in a single html file, Use fontawsome for icons, make the best design and animations possible. Just give the code, no explanations or summary please. where ever image is required use the alt as "Image Here". Don't use markdown for the code, just give the raw text. The exact requirements are given in the following json