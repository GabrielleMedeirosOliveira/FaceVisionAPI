from django.urls import path
from . import views

urlpatterns = [
    path('images/processing/', views.processing, name="images-processing"),
    path('images/processing/<str:id>/image', views.get_image_base64, name="image-return-base64"),
    path('images/processing/<str:id>/image/recognition', views.get_image_recognition, name="image-return-recognition")
]