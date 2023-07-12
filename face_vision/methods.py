import face_recognition
import requests
import json
import cv2
import base64
import os


def save_image_from_url(image_url, save_directory, file_name):
    response = requests.get(image_url)

    if response.status_code == 200:
        save_path = os.path.join(save_directory, file_name)

        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"Imagem salva em: {save_path}")
    else:
        print("Falha ao obter a imagem. Verifique a URL.")

def facial_recognition(file_name, id):
    analyze_result = False

    image_by_request = face_recognition.load_image_file("./storage/uploads/{}".format(file_name))
    image_by_request = cv2.cvtColor(image_by_request, cv2.COLOR_BGR2RGB)

    registered_user_dir = "./storage/registered_user"
    for image_file in os.listdir(registered_user_dir):
        image_path = os.path.join(registered_user_dir, image_file)
        image_by_directory = face_recognition.load_image_file(image_path)
        image_by_directory = cv2.cvtColor(image_by_directory, cv2.COLOR_BGR2RGB)

        encode_by_request = face_recognition.face_encodings(image_by_request)[0]
        encode_by_directory = face_recognition.face_encodings(image_by_directory)[0]

        comparison_result = face_recognition.compare_faces([encode_by_request], encode_by_directory)
        
        if comparison_result[0]:
            analyze_result = comparison_result[0]
            break

    img1_base64 = image_to_base64("./storage/uploads/{}".format(file_name))
    data = {
        'comparison_result': str(analyze_result),
        'image': img1_base64
    }
    
    json_file_name = "{}.json".format(id)

    save_path = os.path.join("./storage/recognation_results", json_file_name)
    with open(save_path, 'w') as json_file:
        json.dump(data, json_file)

    return analyze_result
      
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
        return encoded_string