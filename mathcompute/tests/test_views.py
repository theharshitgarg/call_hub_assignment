import unittest
from django.test import TestCase
from django.shortcuts import reverse
import json

class TestMathComputeViews(TestCase):

    def test_fib_number_view(self):
        url = "http://localhost:8000/compute/math/fibonacci"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("fibonacci", response.content)
        self.assertTemplateUsed(response, 'fibonacci.html')
    

class TestMathComputeAPI(TestCase):

    def validate_json_response(self, data):
        try:
            json.loads(data)
            return True
        except ValueError as error:
            print("Invalid Response:" + str(error))
            return False

    def test_fib_number_api(self):
        url = reverse('fibonacci_api')
        response = self.client.get(url+'?q=100')

        self.assertEqual(response.status_code, 200)
        self.validate_json_response(response.content.decode('utf-8'))
        

