from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def student_login(request):
    from quizzo.serializers.login import LoginSerializer
    from quizzo.utils.deserialize import deserialize
    request_data = deserialize(LoginSerializer, request.data)

    from quizzo.models.student import Student
    student = Student.login(request_data)
    student_obj = {
        "id": student.id,
        "username": student.user,
        "user_type": "student"
    }
    from quizzo.serializers.id_name import IdNameType
    student_id = IdNameType(**student_obj)
    from quizzo.serializers.id_name import IdNameSerializer
    student_id_serializer = IdNameSerializer(student_id)
    return Response(student_id_serializer.data)
