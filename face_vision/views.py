from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import face_recognition as fr
import requests
import json
import cv2
import base64
import os


@csrf_exempt
def processing(request):
    if request.method == 'POST':
        body = request.body
        body_str = body.decode('utf-8')
        json_data = json.loads(body_str)

        image_url = json_data['image_url']
        file_name = json_data["file_name"]
        save_image_from_url(image_url, "./directory", file_name)
        comparison_result = facial_recognition(file_name)

        # Convert images to base64
        img1_base64 = image_to_base64("./directory/{}".format(file_name))
        img2_base64 = image_to_base64("./directory/Jonh Travolta.jpg")

        # Create dictionary to store data
        data = {
            'image1': img1_base64,
            'image2': img2_base64,
            'comparison_result': str(comparison_result)
        }

        # Save data to JSON file
        with open('result.json', 'w') as json_file:
            json.dump(data, json_file)

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
    image_by_directory = fr.load_image_file("./directory/Jonh Travolta.jpg")
    image_by_directory = cv2.cvtColor(image_by_directory,cv2.COLOR_BGR2RGB)

    face_localization = fr.face_locations(image_by_request)[0]
    #cv2.rectangle(image_by_request,(face_localization[3],face_localization[0]),(face_localization[1], face_localization[2]),(0,255,0),2)

    face_localization2 = fr.face_locations(image_by_directory)[0]
    #cv2.rectangle(image_by_directory,(face_localization2[3],face_localization2[0]),(face_localization2[1], face_localization2[2]),(0,255,0),2)

    encode_by_request = fr.face_encodings(image_by_request)[0]
    encode_by_directory = fr.face_encodings(image_by_directory)[0]

    comparison_result = fr.compare_faces([encode_by_request], encode_by_directory)

    cv2.waitKey(0) 
    print(comparison_result)
    return comparison_result
      

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
        return encoded_string