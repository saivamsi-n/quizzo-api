from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def get_student_list(request):
    from quizzo.serializers.limit_offset_search import LimitOffsetSearchSerializer
    from quizzo.utils.deserialize import deserialize
    request_data = deserialize(LimitOffsetSearchSerializer, request.data)

    from quizzo.models.student import Student
    if request_data.filter_by == "all":
        student_query_set = Student.objects.all().values('id', 'username', 'year')
    else:
        student_query_set = Student.objects.filter(username__icontains=request_data.search).values('id', 'username',
                                                                                                   'year')
    total = student_query_set.count()
    students_obj = {
        "total": total,
        "students": student_query_set[request_data.offset:request_data.limit + request_data.offset]
    }
    from quizzo.serializers.teacher_list_response import StudentListResponseType
    students_type_obj = StudentListResponseType(**students_obj)
    from quizzo.serializers.teacher_list_response import StudentListResponseSerializer
    result = StudentListResponseSerializer(students_type_obj)
    return Response(result.data)
