from django.core.urlresolvers import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient


class GetNextQuizAPITestCase02(TestCase):
    """
    Test case to check the attempt status of student of a particular quiz if student didn"t take the test.
    """

    def setUp(self):
        from quizzo.utils.test_case_utils import create_quiz, create_student, create_questions
        self.quiz_obj = create_quiz("quiz1")
        self.student_obj = create_student("test1")
        questions = create_questions()
        self.quiz_obj.questions.add(questions)

    def test_case(self):
        # get API response
        client = APIClient()
        url = reverse("get_quiz", kwargs={"username": self.student_obj.username, "quiz_id": self.quiz_obj.id})
        response = self.client.get(url, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.content)
        self.assertEqual(response.content,
                         b'{"quiz_questions":[{"options":[{"option_id":1,"option":"3.14"},{"option_id":2,"option":"3.33"},{"option_id":3,"option":"3.89"}],"question_id":1,"question":"value of pi?","question_type":"mcq"}],"total":1,"description":"testdescription","title":"quiz1"}')
