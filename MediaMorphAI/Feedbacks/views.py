from django.http import JsonResponse
from django.shortcuts import render
from .models import Feedback
from django.contrib.auth.decorators import login_required

@login_required
def submit_feedback(request):
    feedbacks = Feedback.objects.all()
    is_superuser = request.user.is_superuser
    return render(request, 'feedbacks.html', {
        'feedbacks': feedbacks,
        'is_superuser':is_superuser,
    })