from django.core.urlresolvers import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient


class TeacherProfileUpdateAPITestCase01(TestCase):

    def setUp(self):
        from quizzo.utils.test_case_utils import create_teacher
        self.teacher_obj = create_teacher("test1")

    def test_case(self):
        # get API response
        client = APIClient()
        request = {}
        url = reverse('teacher_profile_update', kwargs={'username': self.teacher_obj.username})
        response = self.client.post(url, content_type='application/json', data=request, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
