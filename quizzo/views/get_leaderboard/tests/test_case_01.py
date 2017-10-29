from django.core.urlresolvers import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient


class GetLeaderBoardAPITestCase01(TestCase):
    '''
    Test case to check the http method.
    '''

    def setUp(self):
        from quizzo.utils.test_case_utils import create_student, create_quiz, create_studentquiz
        self.student_obj = create_student("test_user")
        self.quiz_obj = create_quiz("quiz1")
        self.studentquiz_obj = create_studentquiz(self.student_obj, self.quiz_obj)

    def test_case(self):
        # get API response
        client = APIClient()
        url = reverse('get_leaderboard')
        data = {
            "filter_by": "all",
            "limit": 10,
            "offset": 0,
            "search": ""
        }
        response = self.client.get(url, content_type='application/json', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
