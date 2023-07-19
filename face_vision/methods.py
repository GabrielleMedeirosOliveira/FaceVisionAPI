import face_recognition
import requests
import json
import cv2
import base64
import os
import asyncio


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
    
def image_by_camera(file_name, id):
    xml_haar_cascade = "haarcascade_frontalface_alt2.xml"
    
    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + xml_haar_cascade
    )

    capture = cv2.VideoCapture(0)

    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 120)

    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 80)

    ret, frame_color = capture.read()
    
    faces = face_classifier.detectMultiScale(
        frame_color, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame_color, (x, y), (x + w, y + h), (0, 255, 0), 4)

    cv2.imshow("face", frame_color)

    if ret:
        directory = "./storage/uploads/"
        directory_complete = directory + file_name

        cv2.imwrite(directory_complete, frame_color)

        print("Imagem salva com sucesso em", directory_complete)
    else:
        print("Erro ao capturar o quadro")

    capture.release()
    cv2.destroyAllWindows()
    facial_recognition(file_name, id)
