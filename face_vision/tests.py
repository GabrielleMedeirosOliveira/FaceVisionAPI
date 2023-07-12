import json
import os
from django.http import HttpResponse
from django.test import RequestFactory, TestCase
import unittest
from unittest.mock import patch
from .views import processing, get_image_base64, get_image_recognition
from .methods import save_image_from_url, facial_recognition, image_to_base64


class FaceVisionApiTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_processing_view(self):
        # Prepare the request
        url = '/api/process_image/'
        data = {
            "id": "1",
            "file_name":"Bruce-Banner.jpg",
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrjOK9OLuYSJjhw9eQwvYTWu7Y5FQOHoSTCg&usqp=CAU.jpg"
        }
        body = json.dumps(data).encode('utf-8')
        request = self.factory.post(url, body, content_type='application/json')

        # Call the view function
        response = processing(request)

        # Assert the response
        self.assertEqual(response.status_code, 200)

    def test_get_image_base64_view(self):
        # Prepare the request
        url = '/api/process_image/1'
        request = self.factory.get(url)

        # Call the view function
        response = get_image_base64(request, id=1)

        # Assert the response
        self.assertEqual(response.status_code, 200)

    def test_get_image_recognition_view(self):
        # Prepare the request
        url = '/api/process_image/1/result'
        request = self.factory.get(url)

        # Call the view function
        response = get_image_recognition(request, id=1)

        # Assert the response
        self.assertEqual(response.status_code, 200)
    
    def test_save_image_from_url_success(self):
        # Mock the requests module to return a successful response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.content = b"dummy image content"

        with patch('requests.get', return_value=mock_response):
            save_image_from_url("http://example.com/image.jpg", "./storage/uploads", "image.jpg")

    def test_save_image_from_url_failure(self):
        # Mock the requests module to return a failed response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404

        with patch('requests.get', return_value=mock_response):
            save_image_from_url("http://example.com/image.jpg", "./storage/uploads", "image.jpg")

    def test_facial_recognition_comparison_true(self):
        # Mock a successful comparison result
        mock_load_image_file = unittest.mock.Mock()
        mock_load_image_file.return_value = "dummy image"

        mock_face_encodings = unittest.mock.Mock()
        mock_face_encodings.return_value = ["dummy encoding"]

        mock_compare_faces = unittest.mock.Mock()
        mock_compare_faces.return_value = [True]

        # Mock the necessary functions and objects
        with patch('face_recognition.load_image_file', new=mock_load_image_file), \
             patch('cv2.cvtColor'), \
             patch('os.listdir', return_value=["registered_user.jpg"]), \
             patch('face_recognition.face_encodings', new=mock_face_encodings), \
             patch('face_recognition.compare_faces', new=mock_compare_faces), \
             patch('json.dump') as mock_json_dump:

            result = facial_recognition("image.jpg", "2")

        self.assertTrue(result)
        mock_json_dump.assert_called_once()

    def test_facial_recognition_comparison_false(self):
        # Mock a failed comparison result
        mock_load_image_file = unittest.mock.Mock()
        mock_load_image_file.return_value = "dummy image"

        mock_face_encodings = unittest.mock.Mock()
        mock_face_encodings.return_value = ["dummy encoding"]

        mock_compare_faces = unittest.mock.Mock()
        mock_compare_faces.return_value = [False]

        # Mock the necessary functions and objects
        with patch('face_recognition.load_image_file', new=mock_load_image_file), \
             patch('cv2.cvtColor'), \
             patch('os.listdir', return_value=["registered_user.jpg"]), \
             patch('face_recognition.face_encodings', new=mock_face_encodings), \
             patch('face_recognition.compare_faces', new=mock_compare_faces), \
             patch('json.dump') as mock_json_dump:

            result = facial_recognition("image.jpg", "2")

        self.assertFalse(result)
        mock_json_dump.assert_called_once()

    def test_facial_recognition_no_registered_user(self):
        # Mock an empty directory for registered users
        with patch('face_recognition.load_image_file'), \
             patch('cv2.cvtColor'), \
             patch('os.listdir', return_value=[]), \
             patch('json.dump') as mock_json_dump:

            result = facial_recognition("image.jpg", "2")

        self.assertFalse(result)
        mock_json_dump.assert_called_once()

