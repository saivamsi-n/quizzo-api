from rest_framework import serializers


class QuizTitleType(object):
    def __init__(self, title, **kwargs):
        self.title = title

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class QuizTitleSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)

    def create(self, validated_data):
        return QuizTitleType(**validated_data)
