from rest_framework import serializers


class LeaderboardResponseType(object):
    def __init__(self, points, school, username=None, **kwargs):
        self.username = username
        self.points = points
        self.school = school

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class LeaderboardResponseSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    points = serializers.IntegerField(required=True)
    school = serializers.CharField(required=True)

    def create(self, validated_data):
        return LeaderboardResponseType(**validated_data)
