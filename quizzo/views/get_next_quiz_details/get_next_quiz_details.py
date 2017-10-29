from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def next_quiz(request):
    from quizzo.models.quiz import Quiz
    next_quiz_obj = Quiz.get_next_quiz()
    time = next_quiz_obj.time.strftime('%m/%d/%Y')
    from quizzo.utils.date_time_functions import format_date_string
    time = format_date_string(time)
    quiz = {
        "quiz_id": next_quiz_obj.id,
        "time": time
    }
    return Response(quiz)
