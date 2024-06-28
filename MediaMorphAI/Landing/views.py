from django.shortcuts import render

# Create your views here.
def landing(request):
    # TODO: HANDLE CONTACT FORM TO SUBMIT THE DATA TO THE DATABASE
    return render(request, 'index.html')