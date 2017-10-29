from rest_framework import serializers

from quizzo.utils.deserialize import deserialize


class QuizResponseType(object):
    def __init__(self, quiz_questions=None, total=None, title=None, description=None, **kwargs):
        self.quiz_questions = quiz_questions
        self.total = total
        self.title = title
        self.description = description

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class QuizResponseSerializer(serializers.Serializer):
    from quizzo.serializers.question_options import QuestionOptionSerializer
    quiz_questions = QuestionOptionSerializer(required=False, many=True)
    total = serializers.IntegerField()
    description = serializers.CharField()
    title = serializers.CharField()

    def create(self, validated_data):
        print(validated_data)
        from quizzo.serializers.question_options import QuestionOptionSerializer
        quiz_questions_val = []
        quiz_questions_list_val = validated_data.pop("quiz_questions", [])
        for each_data in quiz_questions_list_val:
            each_obj = deserialize(QuestionOptionSerializer, each_data, many=False, partial=True)
            quiz_questions_val.append(each_obj)

        return QuizResponseType(quiz_questions=quiz_questions_val, **validated_data)
