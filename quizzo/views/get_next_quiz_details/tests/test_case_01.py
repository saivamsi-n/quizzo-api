from django.core.urlresolvers import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from mock import mock

class GetNextQuizDetailsAPITestCase01(TestCase):
    '''
    Test case to check the attempt status of student of a particular quiz if student didn't take the test.
    '''

    def setUp(self):
        from quizzo.utils.test_case_utils import create_quiz
        self.quiz_obj = create_quiz("quiz1")


    def test_case(self):
        # get API response
        client = APIClient()
        url = reverse('next_quiz')
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
