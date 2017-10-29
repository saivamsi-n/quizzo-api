from rest_framework.decorators import api_view
from rest_framework.response import Response
from quizzo.models.student import Student


@api_view(['POST'])
def get_leaderboard(request):
    from quizzo.serializers.limit_offset_search import LimitOffsetSearchSerializer
    from quizzo.utils.deserialize import deserialize
    request_data = deserialize(LimitOffsetSearchSerializer, request.data)
    from quizzo.utils.constants import LeaderBoardSearchTypes
    if request_data.filter_by == LeaderBoardSearchTypes.school.value:
        student_query_set = Student.objects.filter(school__icontains=request_data.search)
    elif request_data.filter_by == LeaderBoardSearchTypes.city.value:
        student_query_set = Student.objects.filter(city__icontains=request_data.search)
    else:
        student_query_set = Student.objects.all()
    final_result_list = list()
    print("after stundet")
    from django.db.models import Sum
    for obj in student_query_set:
        q = obj.studentquiz_set.aggregate(total_marks=Sum("marks_obtained"))
        temp = {"username": obj.username, "school": obj.school, "points": q['total_marks']}
        final_result_list.append(temp)
    final_result_list[:] = [d for d in final_result_list if d.get('points') is not None]
    final_result_list = sorted(final_result_list, key=lambda k: k['points'], reverse=True)
    students_obj = {
        "total": len(final_result_list),
        "students": final_result_list[request_data.offset:request_data.offset + request_data.limit]
    }

    from quizzo.serializers.leaderboard_list_response import LeaderboardResponseListType
    students_type_obj = LeaderboardResponseListType(**students_obj)
    from quizzo.serializers.leaderboard_list_response import LeaderboardListResponseSerializer
    result = LeaderboardListResponseSerializer(students_type_obj)
    return Response(result.data)
