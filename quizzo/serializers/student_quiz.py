from rest_framework import serializers


class StudentQuizType(object):
    def __init__(self, marks, title, grade, **kwargs):
        self.marks = marks
        self.title = title
        self.grade = grade

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class StudentQuizSerializer(serializers.Serializer):
    title = serializers.CharField()
    marks = serializers.IntegerField()
    grade = serializers.CharField(required=False)

    def create(self, validated_data):
        return StudentQuizType(**validated_data)
