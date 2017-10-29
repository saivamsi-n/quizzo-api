from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def get_student_quiz_list(request, username):
    from quizzo.serializers.limit_offset import LimitOffsetSerializer
    from quizzo.utils.deserialize import deserialize
    request_data = deserialize(LimitOffsetSerializer, request.data)

    from quizzo.models.student import Student
    student_obj = Student.get_student_obj(username)

    from quizzo.models.student_quiz import StudentQuiz
    student_query_set = StudentQuiz.objects.filter(student=student_obj)[
                        request_data.offset:request_data.limit + request_data.offset]

    students_list = []
    for obj in student_query_set:
        temp = {
            "title": obj.quiz.title,
            "marks": obj.marks_obtained,
            "grade": obj.grade
        }
        students_list.append(temp)
    total = student_query_set.count()
    students_obj = {
        "total": total,
        "quizzes": students_list
    }
    from quizzo.serializers.student_quiz_list import StudentQuizListType
    students_type_obj = StudentQuizListType(**students_obj)
    from quizzo.serializers.student_quiz_list import StudentQuizListResponseSerializer
    result = StudentQuizListResponseSerializer(students_type_obj)
    return Response(result.data)
