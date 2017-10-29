from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['get'])
def check_student_quiz_attempt(request, username, quiz_id):
    from quizzo.models.student_quiz import StudentQuiz
    result = StudentQuiz.check_user_attempt(username, quiz_id)
    return Response(result)
