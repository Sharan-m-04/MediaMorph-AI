from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from openai import OpenAI
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import requests

@csrf_exempt
@login_required
def generateimage(request):
    if request.method == 'POST':
        try:
            prompt = request.POST['prompt']
            client = OpenAI(api_key=settings.SECRET_KEY)
            response = client.images.generate(
                model="dall-e-2",
                prompt=prompt,
                size="256x256",
                n=1,
            )
            image_url = response.data[0].url
            return JsonResponse({'image_url': image_url})
        except Exception as e:
            print(f"Error generating image: {e}")
            return JsonResponse({'err_msg': 'Failed to generate Image'}, status=500)
    return render(request, 'generateImage.html')
