from rest_framework import serializers

from quizzo.utils.deserialize import deserialize


class StudentQuizListType(object):
    def __init__(self, total=None, quizzes=None, **kwargs):
        self.total = total
        self.quizzes = quizzes

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class StudentQuizListResponseSerializer(serializers.Serializer):
    from quizzo.serializers.student_quiz import StudentQuizSerializer
    quizzes = StudentQuizSerializer(required=False, many=True)
    total = serializers.IntegerField()

    def create(self, validated_data):
        from quizzo.serializers.student_quiz import StudentQuizSerializer
        quizzes_val = []
        quizzes_list_val = validated_data.pop("quizzes", [])
        for each_data in quizzes_list_val:
            each_obj = deserialize(StudentQuizSerializer, each_data, many=False, partial=True)
            quizzes_val.append(each_obj)

        return StudentQuizListType(quizzes=quizzes_val, **validated_data)
