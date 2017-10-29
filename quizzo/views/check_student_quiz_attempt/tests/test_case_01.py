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
        self.student_obj = create_student("test_user_01")
        self.quiz_obj = create_quiz("quiz1")
        self.studentquiz_obj_01 = create_studentquiz(self.student_obj, self.quiz_obj)
        self.student_obj_02 = create_student("test_user_02")
        self.studentquiz_obj_02 = create_studentquiz(self.student_obj_02, self.quiz_obj)

    def test_case(self):
        # get API response
        client = APIClient()
        url = reverse('student_quiz_attempt_check',
                      kwargs={'quiz_id': self.quiz_obj.id, 'username': self.student_obj.username})
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, b'"true"')
