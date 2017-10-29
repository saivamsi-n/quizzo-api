from django.core.urlresolvers import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient


class CheckStudentQuizAttemptAPITestCase01(TestCase):
    '''
    Test case to check the attempt status of student of a particular quiz if student didn't take the test.
    '''

    def setUp(self):
        from quizzo.utils.test_case_utils import create_student, create_quiz, create_studentquiz
        self.student_obj = create_student("testuser_02")
        self.quiz = create_quiz("title")

    def test_case(self):
        # get API response
        client = APIClient()
        url = reverse('student_quiz_attempt_check',
                      kwargs={'quiz_id': self.quiz.id, 'username': self.student_obj.username})
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, b'"false"')
