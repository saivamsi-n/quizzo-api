from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def check_quiz_present(request):
    from quizzo.models.quiz import Quiz
    check = Quiz.check_quiz_present()
    quiz = {
        "check": check
    }
    return Response(quiz)
