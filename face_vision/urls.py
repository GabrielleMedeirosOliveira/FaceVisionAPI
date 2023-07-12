from django.urls import path
from . import views

urlpatterns = [
    path('process_image/', views.processing, name="images-processing"),
    path('process_image/<str:id>/', views.get_image_base64, name="image-return-base64"),
    path('process_image/<str:id>/result', views.get_image_recognition, name="image-return-recognition")
]