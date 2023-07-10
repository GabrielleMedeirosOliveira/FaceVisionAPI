from django.urls import path
from .views import DefaultReturns

urlpatterns = [
    path('hello/', DefaultReturns.hello_world, name="hello"),
]