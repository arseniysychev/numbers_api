from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import NumberCounter


class NumberCounterAPITests(APITestCase):
    """
    API Tests for NumberCounter.
    """
    data_valid_data = [1, 5, 3, 5, 3, 1, 6]

    def send_unpaired_data(self, data_array):
        url = reverse('send_unpaired')
        data = {"data": data_array}
        return self.client.post(url, data, format='json')

    def test_create_number(self):
        response = self.send_unpaired_data(self.data_valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'answer': 6})
        self.assertEqual(NumberCounter.objects.count(), 1)
        self.assertEqual(NumberCounter.objects.get(number=6).count, 1)

    def test_create_number_with_empty_list(self):
        response = self.send_unpaired_data([])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'data': ["Can't be empty list."]})

    def test_create_number_without_odd(self):
        response = self.send_unpaired_data([1, 5, 3, 5, 3, 1])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'data': ['Data list not include odd value.']})

    def test_create_number_with_multiple_odd(self):
        response = self.send_unpaired_data([1, 5, 3, 5, 3, 1, 6, 7])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'data': ['Too many odd values.']})

    def test_get_statistic(self):
        self.send_unpaired_data(self.data_valid_data)
        url = reverse('get_statistic')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{"number": 6, "count": 1}])
