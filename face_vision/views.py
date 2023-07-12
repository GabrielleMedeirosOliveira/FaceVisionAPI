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
    #Receives data (image, URL and id) by POST method and converts to string
    if request.method == 'POST':
        body = request.body
        body_str = body.decode('utf-8')
        json_data = json.loads(body_str)

        image_url = json_data['image_url']
        file_name = json_data["file_name"]
        id = json_data["id"]
        save_image_from_url(image_url, "./directory/uploads", file_name)
        comparison_result = facial_recognition(file_name,id)

        #Returns an HTTP response with a 200 status code
        return HttpResponse(status=200)
    
def save_image_from_url(image_url, save_directory, file_name):
    response = requests.get(image_url)
    
    #Save image received by url and save in a specific folder. Checking if the url is correct, informing if it was saved or not

    if response.status_code == 200:
        save_path = os.path.join(save_directory, file_name)

        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"Imagem salva em: {save_path}")
    else:
        print("Falha ao obter a imagem. Verifique a URL.")

def facial_recognition(file_name,id):
    analyze_result = False

    # Receives the uploaded image and performs image color correction
    image_by_request = fr.load_image_file("./directory/uploads/{}".format(file_name))
    image_by_request = cv2.cvtColor(image_by_request, cv2.COLOR_BGR2RGB)

    #Defines a dictionary, which contains the image of registered users, then running a loop, for each image in the directory

    registered_user_dir = "./directory/registered_user"
    for image_file in os.listdir(registered_user_dir):
        image_path = os.path.join(registered_user_dir, image_file)
        image_by_directory = fr.load_image_file(image_path)
        image_by_directory = cv2.cvtColor(image_by_directory, cv2.COLOR_BGR2RGB)

        #face_localization = fr.face_locations(image_by_request)[0]
        #face_localization2 = fr.face_locations(image_by_directory)[0]

        #Calculates the face encoding of the image from both the uploaded image and the image in the directory

        encode_by_request = fr.face_encodings(image_by_request)[0]
        encode_by_directory = fr.face_encodings(image_by_directory)[0]

        #Compare the face encodings of the two images

        comparison_result = fr.compare_faces([encode_by_request], encode_by_directory)

        cv2.waitKey(0) 
        print("Image:", image_file)
        print(comparison_result)

        #If the comparison indicates that the faces match the "analyze_result" variable is set to "True" and the loop is stopped.

        if comparison_result[0]:
            analyze_result = comparison_result[0]
            break

    img1_base64 = image_to_base64("./directory/uploads/{}".format(file_name))
    data = {
        'image': img1_base64,
        'comparison_result': str(analyze_result)
    }
    
    # Generate a unique file name for the JSON file
    json_file_name = "{}.json".format(id)

    # Save data to JSON file
    save_path = os.path.join("./directory/recognation_results", json_file_name)
    with open(save_path, 'w') as json_file:
        json.dump(data, json_file)

    return analyze_result
      
#Transforms the received image into base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
        return encoded_string

@csrf_exempt
def get_image_base64(request, id):
    if request.method == 'GET':
        file_path = f"./directory/recognation_results/{id}.json"

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
        file_path = f"./directory/recognation_results/{id}.json"

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)

            if data:
                json_data = json.dumps(data)
                return HttpResponse(json_data, status=200, content_type="application/json")

        return HttpResponse(status=204)