from django.urls import path
from .views import Image

urlpatterns = [
    path('images/processing/', Image.processing, name="images-processing"),
]