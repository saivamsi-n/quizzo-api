from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def get_user_info(request):
    from quizzo.serializers.id_name import IdNameSerializer
    from quizzo.utils.deserialize import deserialize
    request_data = deserialize(IdNameSerializer, request.data)

    from quizzo.models.student import Student
    from quizzo.models.teacher import Teacher
    if request_data.user_type == "student":
        obj = Student.get_student_details(id=request_data.id)
    else:
        obj = Teacher.get_teacher_details(id=request_data.id)

    from quizzo.serializers.profile import ProfileType
    students_type_obj = ProfileType(**obj)
    from quizzo.serializers.profile import ProfileSerializer
    result = ProfileSerializer(students_type_obj)
    return Response(result.data)
