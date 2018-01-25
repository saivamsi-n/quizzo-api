from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_quiz(request, username, quiz_id):
    from quizzo.models.quiz import Quiz
    quiz_obj = Quiz.objects.get(id=quiz_id)
    quiz_questions = []
    all_questions = quiz_obj.questions.all().prefetch_related('options')
    for obj in all_questions:
        options_list = []
        for each_obj in obj.options.all():
            temp = {
                "option_id": each_obj.id,
                "option": each_obj.content
            }
            options_list.append(temp)
        questions_temp = {
            "question_id": obj.id,
            "question": obj.question_content,
            "options": options_list,
            "question_type": obj.type
        }
        quiz_questions.append(questions_temp)
    quiz_dict = {
        "total": all_questions.count(),
        "quiz_questions": quiz_questions,
        "description": quiz_obj.description,
        "title": quiz_obj.title,
        "duration": quiz_obj.duration,
    }
    from quizzo.serializers.quiz_response import QuizResponseType
    final_obj = QuizResponseType(**quiz_dict)
    from quizzo.serializers.quiz_response import QuizResponseSerializer
    result = QuizResponseSerializer(final_obj)
    return Response(result.data)
