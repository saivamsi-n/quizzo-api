from rest_framework import serializers

from quizzo.utils.deserialize import deserialize


class QuizAttemptListType(object):
    def __init__(self, quiz_questions=None, total=None, **kwargs):
        self.quiz_questions = quiz_questions
        self.total = total

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class QuizAttemptListSerializer(serializers.Serializer):
    from quizzo.serializers.quiz_attempt import QuizAttemptResponseSerializer
    quiz_questions = QuizAttemptResponseSerializer(required=False, many=True)
    total = serializers.CharField(required=False)

    def create(self, validated_data):
        from quizzo.serializers.quiz_attempt import QuizAttemptResponseSerializer
        quiz_questions_val = []
        quiz_questions_list_val = validated_data.pop("quiz_questions", [])
        for each_data in quiz_questions_list_val:
            each_obj = deserialize(QuizAttemptResponseSerializer, each_data, many=False, partial=True)
            quiz_questions_val.append(each_obj)

        return QuizAttemptListType(quiz_questions=quiz_questions_val, **validated_data)
