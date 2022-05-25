from unittest import TestCase
import requests


class Test(TestCase):
    base = 'http://localhost:8000/'

    def test_home(self):
        r = requests.get(self.base)
        self.assertEqual(r.status_code, 200)
        response = r.json()
        self.assertEqual(response['message'], 'Technical test for Platanomelon.')

    def test_prediction(self):
        body = [
                {
                    "Asymmetry coefficient": 1.018,
                    "Perimeter": 14.57,
                    "Length of kernel": 5.554,
                    "Compactness": 0.8811,
                    "Area": 14.88,
                    "Length kernel groove": 4.956,
                    "Width of kernel": 3.333
                },
                {
                    "Asymmetry coefficient": 4.972,
                    "Perimeter": 14.89,
                    "Length of kernel": 5.776,
                    "Compactness": 0.8823,
                    "Area": 15.56,
                    "Length kernel groove": 5.847,
                    "Width of kernel": 3.408
                }
        ]
        r = requests.post(self.base + 'predict', json=body)
        print(r.json())
        self.assertEqual(r.status_code, 200)
        response = r.json()
        #self.assertEqual(response['prediction'], ['1', '0'])
