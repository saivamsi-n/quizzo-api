from rest_framework import serializers

from quizzo.utils.deserialize import deserialize


class QuizReferenceType(object):
    def __init__(self, question=None, question_id=None, options=None, question_type=None, user_answer=None,
                 user_answer_id=None, correct_answer=None, correct_answer_id=None, **kwargs):
        self.question = question
        self.question_id = question_id
        self.options = options
        self.question_type = question_type
        self.user_answer = user_answer
        self.user_answer_id = user_answer_id
        self.correct_answer = correct_answer
        self.correct_answer_id = correct_answer_id

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class QuizReferenceResponseSerializer(serializers.Serializer):
    from quizzo.serializers.option import OptionSerializer
    options = OptionSerializer(required=False, many=True)
    question_id = serializers.IntegerField(required=False)
    question = serializers.CharField()
    question_type = serializers.CharField()
    user_answer = serializers.CharField()
    user_answer_id = serializers.IntegerField()
    correct_answer = serializers.CharField()
    correct_answer_id = serializers.IntegerField()

    def create(self, validated_data):
        from quizzo.serializers.option import OptionSerializer
        options_val = []
        options_list_val = validated_data.pop("options", [])
        for each_data in options_list_val:
            each_obj = deserialize(OptionSerializer, each_data, many=False, partial=True)
            options_val.append(each_obj)

        return QuizReferenceType(options=options_val, **validated_data)
