from rest_framework import serializers
from quizzo.serializers.question_options import QuestionOptionSerializer


class QuizAttemptResponseType(object):
    def __init__(self, type=None, question_id=None, option_id=None, option=None, **validated_data):
        self.question_id = question_id
        self.option = option
        self.option_id = option_id
        self.type = type

        def __unicode__(self):
            return str(self)

        def __str__(self):
            return str(self).encode('utf-8')

        def __getitem__(self, item):
            return getattr(self, item)


class QuizAttemptResponseSerializer(serializers.Serializer):
    question_id = serializers.IntegerField(required=False)
    option = serializers.CharField(required=False)
    option_id = serializers.IntegerField(required=False)
    type = serializers.CharField(required=False)

    def create(self, validate_data):
        return QuizAttemptResponseType(**validate_data)
