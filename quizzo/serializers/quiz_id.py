from rest_framework import serializers


class QuizIdType(object):
    def __init__(self, id=None, **kwargs):
        self.quiz_id = id

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class QuizIdSerializer(serializers.Serializer):
    quiz_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return QuizIdType(**validated_data)
