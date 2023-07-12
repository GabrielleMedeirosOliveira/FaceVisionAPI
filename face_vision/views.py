from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from . import methods


@csrf_exempt
def processing(request):
    if request.method == 'POST':
        body = request.body
        body_str = body.decode('utf-8')
        json_data = json.loads(body_str)

        image_url = json_data['image_url']
        file_name = json_data["file_name"]
        id = json_data["id"]
        methods.save_image_from_url(image_url, "./storage/uploads", file_name)
        methods.facial_recognition(file_name, id)

        return HttpResponse(status=200)
    
@csrf_exempt
def get_image_base64(request, id):
    if request.method == 'GET':
        file_path = f"./storage/recognation_results/{id}.json"

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                image_base64 = data.get('image')

            if image_base64:
                data = {
                    'image': image_base64
                }
                json_data = json.dumps(data)
                return HttpResponse(json_data, status=200, content_type="application/json")

        return HttpResponse(status=204)

@csrf_exempt
def get_image_recognition(request, id):
    if request.method == 'GET':
        file_path = f"./storage/recognation_results/{id}.json"

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)

            if data:
                json_data = json.dumps(data)
                return HttpResponse(json_data, status=200, content_type="application/json")

        return HttpResponse(status=204)
    
