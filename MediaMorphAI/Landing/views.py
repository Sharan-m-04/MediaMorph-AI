from django.shortcuts import redirect, render
from Feedbacks.models import Feedback

def landing(request):
    # TODO: HANDLE CONTACT FORM TO SUBMIT THE DATA TO THE DATABASE
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        new_feedback = Feedback(name=name, email=email, message=message)
        new_feedback.save()
        return redirect('/')
    else:
        return render(request, 'index.html')
