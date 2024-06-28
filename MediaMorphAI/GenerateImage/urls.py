from django.urls import path
from .views import generateimage, download_image

urlpatterns = [
    path('', generateimage, name='generateimage'),
    # path('download_image/', download_image, name='download_image'),
]
