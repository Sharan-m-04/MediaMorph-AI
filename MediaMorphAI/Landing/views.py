from django.shortcuts import redirect, render
from Feedbacks.models import Feedback

def landing(request):
    if request.method == 'POST':
        isSaved = False
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        new_feedback = Feedback(name=name, email=email, message=message)
        new_feedback.save()
        isSaved = True
        return redirect('/', {'isSaved':isSaved})
    else:
        return render(request, 'index.html')
