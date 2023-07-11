from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


class Image:
    @csrf_exempt
    def processing(request):
        if request.method == 'POST':
            body = request.body
            body_str = body.decode('utf-8')
            json_data = json.loads(body_str)
            
            image_url = json_data['img']
            Image.facial_recognition(image_url)

            return HttpResponse(status=200)
        
    def facial_recognition(image_url):
        print(image_url)

