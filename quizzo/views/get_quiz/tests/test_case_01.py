from django.core.urlresolvers import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient


class GetNextQuizAPITestCase01(TestCase):
    '''
    Test case to check the attempt status of student of a particular quiz if student didn't take the test.
    '''

    def setUp(self):
        from quizzo.utils.test_case_utils import create_quiz, create_student
        self.quiz_obj = create_quiz("quiz1")
        self.student_obj = create_student("test1")

    def test_case(self):
        # get API response
        client = APIClient()
        url = reverse('get_quiz', kwargs={'username': self.student_obj.username, 'quiz_id': self.quiz_obj.id})
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content,
                         b'{"quiz_questions":[],"total":0,"description":"testdescription","title":"quiz1"}')
