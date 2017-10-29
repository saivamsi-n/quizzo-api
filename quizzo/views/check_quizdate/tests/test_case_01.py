from django.core.urlresolvers import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient


class CheckQuizDateAPITestCase01(TestCase):
    '''
    Test case to check the response the realative time to attemptquiz.
    '''

    def setUp(self):
        from quizzo.models.quiz import Quiz
        from datetime import datetime
        Quiz.objects.create(title="test quiz", description="test description", time=datetime.now())

    def test_case(self):
        # get API response
        client = APIClient()
        url = reverse('quiz_date_check', kwargs={'quiz_id': 1, 'username': 'test_user'})
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, b'{"check":"true"}')
