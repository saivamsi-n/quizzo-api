from django.core.urlresolvers import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient


class QuizAttemptAPITestCase01(TestCase):
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
        request = {"total": 0, "quiz_question": 0}
        url = reverse('quiz_attempt', kwargs={'username': self.student_obj.id, "quiz_id": self.quiz_obj.id})

        response = self.client.post(url, content_type='application/json', data=request, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
