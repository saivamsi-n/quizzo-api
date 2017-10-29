from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def quizdate_attempt_check(request, username, quiz_id):
    import datetime
    current_time = datetime.datetime.now()
    from quizzo.models.quiz import Quiz
    next_quiz_obj = Quiz.get_quiz_obj(id=quiz_id)
    time = next_quiz_obj.time
    if ((time.replace(tzinfo=None)) > current_time):
        check = "false"
    else:
        check = "true"
    quiz = {
        "check": check
    }
    return Response(quiz)
