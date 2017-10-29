from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def quiz_statistics(request, username):
    from quizzo.serializers.quiz_title import QuizTitleSerializer
    from quizzo.utils.deserialize import deserialize
    request_data = deserialize(QuizTitleSerializer, request.data)

    from quizzo.models.option import Option
    from quizzo.models.student_quiz import StudentQuiz
    from quizzo.models.student import Student
    from quizzo.models.quiz import Quiz
    quiz_obj = StudentQuiz.objects.get(student=Student.objects.get(username=username),
                                       quiz_id=Quiz.objects.get(title=request_data.title).id)

    user_questions = quiz_obj.user_options.all()
    questions_list = []
    for obj in user_questions:

        question_id = obj.question.id
        question_content = obj.question.question_content
        user_answer = obj.attempted_answer
        user_answer_id = obj.attempted_id
        question_type = obj.question.type
        correct_answer_id = obj.question.answer_id
        correct_answer = Option.objects.get(id=obj.question.answer_id).content
        options_list = []
        for each_obj in obj.question.options.all():
            temp = {
                "option_id": each_obj.id,
                "option": each_obj.content
            }
            options_list.append(temp)
        question_temp = {
            "question": question_content,
            "question_id": question_id,
            "user_answer_id": user_answer_id,
            "user_answer": user_answer,
            "question_type": question_type,
            "options": options_list,
            "correct_answer": correct_answer,
            "correct_answer_id": correct_answer_id
        }
        questions_list.append((question_temp))

    total = len(questions_list)
    result = {
        "total": total,
        "questions_list": questions_list
    }
    from quizzo.serializers.quiz_reference_list import QuizReferenceListType
    result_obj = QuizReferenceListType(**result)
    from quizzo.serializers.quiz_reference_list import QuizReferenceListSerializer
    result = QuizReferenceListSerializer(result_obj)
    return Response(result.data)
