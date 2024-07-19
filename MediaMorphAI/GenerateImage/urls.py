from django.urls import path
from .views import generateimage

urlpatterns = [
    path('', generateimage, name='generateimage'),
]
