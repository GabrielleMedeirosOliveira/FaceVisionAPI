from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import face_recognition as fr
import requests
import json
import cv2
import os


@csrf_exempt
def processing(request):
    if request.method == 'POST':
        body = request.body
        body_str = body.decode('utf-8')
        json_data = json.loads(body_str)
        
        image_url = json_data['image_url']
        file_name = json_data["file_name"]
        save_image_from_url(image_url,"./directory",file_name)
        facial_recognition(file_name)

        return HttpResponse(status=200)

def save_image_from_url(image_url, save_directory, file_name):
    response = requests.get(image_url)
    
    if response.status_code == 200:
        save_path = os.path.join(save_directory, file_name)

        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"Imagem salva em: {save_path}")
    else:
        print("Falha ao obter a imagem. Verifique a URL.")

def facial_recognition(file_name):
    image_by_request = fr.load_image_file("./directory/{}".format(file_name))
    image_by_request = cv2.cvtColor(image_by_request,cv2.COLOR_BGR2RGB)
    image_by_directory = fr.load_image_file("./directory/Elon-Musk.jpg")
    image_by_directory = cv2.cvtColor(image_by_directory,cv2.COLOR_BGR2RGB)

    face_localization = fr.face_locations(image_by_request)[0]
    #cv2.rectangle(image_by_request,(face_localization[3],face_localization[0]),(face_localization[1], face_localization[2]),(0,255,0),2)

    face_localization2 = fr.face_locations(image_by_directory)[0]
    #cv2.rectangle(image_by_directory,(face_localization2[3],face_localization2[0]),(face_localization2[1], face_localization2[2]),(0,255,0),2)

    encode_by_request = fr.face_encodings(image_by_request)[0]
    encode_by_directory = fr.face_encodings(image_by_directory)[0]

    comparison_result = fr.compare_faces([encode_by_request], encode_by_directory)

    print(comparison_result)
    return cv2.waitKey(0)