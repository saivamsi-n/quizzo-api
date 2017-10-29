from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def quiz_answers(request, username, quiz_id):
    from quizzo.serializers.quiz_attempt_list import QuizAttemptListSerializer
    from quizzo.utils.deserialize import deserialize
    request_data = deserialize(QuizAttemptListSerializer, request.data)

    from quizzo.models.option import Option
    from quizzo.models.quiz import Quiz
    quiz_obj = Quiz.objects.get(id=quiz_id)

    questions = quiz_obj.questions.all()
    marks_obtained = 0
    for req_obj in request_data.quiz_questions:
        for obj in questions:
            if req_obj.question_id == obj.id:
                if req_obj.type == "mcq":
                    if req_obj.option_id == obj.answer_id:
                        marks_obtained += obj.marks
                        break
                else:
                    if req_obj.option == Option.objects.get(id=obj.answer_id).content:
                        marks_obtained += obj.marks

    total_question_marks = 0
    for obj in questions:
        total_question_marks += obj.marks

    from quizzo.utils.grade_calculator import grade_calculator
    grade = grade_calculator(total_question_marks, marks_obtained)

    from quizzo.models.student_quiz import StudentQuiz
    from quizzo.models.student import Student
    student_obj = Student.get_student_obj(username)
    studentquiz_obj = StudentQuiz.objects.create(
        student=student_obj,
        quiz_id=quiz_id,
        marks_obtained=marks_obtained,
        grade=grade
    )
    from quizzo.models.question import Question
    from quizzo.models.student_quiz_attempt import StudentQuizAttempt
    for obj in request_data.quiz_questions:
        student_attempted_obj = StudentQuizAttempt.objects.create(
            question=Question.get_question_obj(obj.question_id),
            attempted_id=obj.option_id,
            attempted_answer=obj.option
        )
        studentquiz_obj.user_options.add(student_attempted_obj)
    result = {
        "grade": grade,
        "marks": marks_obtained
    }

    return Response(result)
