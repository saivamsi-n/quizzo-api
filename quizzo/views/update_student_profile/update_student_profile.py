from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def update_student_profile(request, username):
    from quizzo.serializers.student_profile import StudentProfileSerializer
    from quizzo.utils.deserialize import deserialize
    student_obj = deserialize(StudentProfileSerializer, request.data)
    from quizzo.models.student import Student
    student = Student.update_profile(student_obj, username)
    student_obj = {
        "id": student.id,
        "username": student.user,
        "user_type": "student"
    }
    from quizzo.serializers.id_name import IdNameType
    student_type_obj = IdNameType(**student_obj)
    from quizzo.serializers.id_name import IdNameSerializer
    student_serializer = IdNameSerializer(student_type_obj)
    return Response(student_serializer.data)
