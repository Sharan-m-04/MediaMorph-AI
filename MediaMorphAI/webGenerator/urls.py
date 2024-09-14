from django.urls import path
from . import views

urlpatterns = [
    path('', views.generateweb),
    path('preview/', views.preview, name='preview'),
]