from rest_framework import serializers

from quizzo.utils.deserialize import deserialize


class QuizReferenceListType(object):
    def __init__(self, questions_list=None, total=None, **kwargs):
        self.questions_list = questions_list
        self.total = total

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class QuizReferenceListSerializer(serializers.Serializer):
    from quizzo.serializers.quiz_reference import QuizReferenceResponseSerializer
    questions_list = QuizReferenceResponseSerializer(required=False, many=True)
    total = serializers.CharField(required=False)

    def create(self, validated_data):
        from quizzo.serializers.quiz_reference import QuizReferenceResponseSerializer
        quiz_questions_val = []
        quiz_questions_list_val = validated_data.pop("questions_list", [])
        for each_data in quiz_questions_list_val:
            each_obj = deserialize(QuizReferenceResponseSerializer, each_data, many=False, partial=True)
            quiz_questions_val.append(each_obj)

        return QuizReferenceListType(questions_list=quiz_questions_val, **validated_data)
