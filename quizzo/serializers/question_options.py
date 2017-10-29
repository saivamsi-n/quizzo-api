from rest_framework import serializers

from quizzo.utils.deserialize import deserialize


class QuestionOptionType(object):
    def __init__(self, question=None, question_id=None, options=None, question_type=None, **kwargs):
        self.question = question
        self.question_id = question_id
        self.options = options
        self.question_type = question_type

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class QuestionOptionSerializer(serializers.Serializer):
    from quizzo.serializers.option import OptionSerializer
    options = OptionSerializer(required=False, many=True)
    question_id = serializers.IntegerField(required=False)
    question = serializers.CharField()
    question_type = serializers.CharField()

    def create(self, validated_data):
        from quizzo.serializers.option import OptionSerializer
        options_val = []
        options_list_val = validated_data.pop("options", [])
        for each_data in options_list_val:
            each_obj = deserialize(OptionSerializer, each_data, many=False, partial=True)
            options_val.append(each_obj)

        return QuestionOptionType(options=options_val, **validated_data)
