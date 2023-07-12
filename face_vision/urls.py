from django.urls import path
from . import views

urlpatterns = [
    path('images/processing/', views.processing, name="images-processing"),
]