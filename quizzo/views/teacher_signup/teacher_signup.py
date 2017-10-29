from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def teacher_signup(request):
    from quizzo.serializers.teacher_profile import TeacherProfileSerializer
    from quizzo.utils.deserialize import deserialize
    teacher_obj = deserialize(TeacherProfileSerializer, request.data)

    from quizzo.models.teacher import Teacher
    teacher = Teacher.sign_up(teacher_obj)
    teacher_obj = {
        "id": teacher.id,
        "username": teacher.user,
        "user_type": "teacher"
    }
    from quizzo.serializers.id_name import IdNameType
    teacher_type_obj = IdNameType(**teacher_obj)

    from quizzo.serializers.id_name import IdNameSerializer
    teacher_serializer = IdNameSerializer(teacher_type_obj)

    return Response(teacher_serializer.data)
