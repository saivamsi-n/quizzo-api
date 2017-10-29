from rest_framework import serializers

from quizzo.utils.deserialize import deserialize


class LeaderboardResponseListType(object):
    def __init__(self, total=None, students=None, **kwargs):
        self.total = total
        self.students = students

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class LeaderboardListResponseSerializer(serializers.Serializer):
    total = serializers.IntegerField(required=False)
    from quizzo.serializers.leaderboard_response import LeaderboardResponseSerializer
    students = LeaderboardResponseSerializer(required=False, many=True)

    def create(self, validated_data):
        from quizzo.serializers.leaderboard_response import LeaderboardResponseSerializer
        students_val = []
        students_list_val = validated_data.pop("students", [])
        for each_data in students_list_val:
            each_obj = deserialize(LeaderboardResponseSerializer, each_data, many=False, partial=True)
            students_val.append(each_obj)

        return LeaderboardResponseListType(students=students_val, **validated_data)
