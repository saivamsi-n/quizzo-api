from rest_framework import serializers


class PointsType(object):
    def __init__(self, points=None, **kwargs):
        self.points = points

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class PointsSerializer(serializers.Serializer):
    points = serializers.IntegerField(required=False)

    def create(self, valpointsated_data):
        return PointsType(**valpointsated_data)
