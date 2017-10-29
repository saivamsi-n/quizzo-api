from django.core.urlresolvers import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient


class GetNextQuizDetailsAPITestCase02(TestCase):
    '''
    Test case to check the attempt status of student of a particular quiz if student didn't take the test.
    '''

    def setUp(self):
        pass

    def test_case(self):
        # get API response
        client = APIClient()
        url = reverse('next_quiz')
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.content, b'{"detail":"No Quiz avaialable"}')
