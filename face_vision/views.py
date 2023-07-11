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
    imgElon = fr.load_image_file("./directory/{}".format(file_name))
    imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
    imgElon2 = fr.load_image_file("./directory/Elon-Musk.jpg")
    imgElon2 = cv2.cvtColor(imgElon2,cv2.COLOR_BGR2RGB)

    faceLoc = fr.face_locations(imgElon)[0]
    #cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1], faceLoc[2]),(0,255,0),2)

    faceLoc2 = fr.face_locations(imgElon2)[0]
    #cv2.rectangle(imgElon2,(faceLoc2[3],faceLoc2[0]),(faceLoc2[1], faceLoc2[2]),(0,255,0),2)

    encodeElon = fr.face_encodings(imgElon)[0]
    encodeElon2 = fr.face_encodings(imgElon2)[0]

    comparacao = fr.compare_faces([encodeElon], encodeElon2)

    print(comparacao)
    return cv2.waitKey(0)