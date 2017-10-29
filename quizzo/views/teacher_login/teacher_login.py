from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def teacher_login(request):
    from quizzo.serializers.login import LoginSerializer
    from quizzo.utils.deserialize import deserialize
    request_data = deserialize(LoginSerializer, request.data)

    from quizzo.models.teacher import Teacher
    teacher = Teacher.login(request_data)
    teacher_obj = {
        "id": teacher.id,
        "username": teacher.user,
        "user_type": "teacher"
    }
    from quizzo.serializers.id_name import IdNameType
    teacher_id = IdNameType(**teacher_obj)

    from quizzo.serializers.id_name import IdNameSerializer
    teacher_id_serializer = IdNameSerializer(teacher_id)

    return Response(teacher_id_serializer.data)
