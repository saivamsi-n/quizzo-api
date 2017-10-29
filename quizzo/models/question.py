from __future__ import unicode_literals
from django.db import models
from .option import Option
from quizzo.utils.constants import OptionChoices


class Question(models.Model):
    question_content = models.TextField(null=False, blank=False)
    marks = models.IntegerField(null=False)
    options = models.ManyToManyField(Option)
    answer_id = models.IntegerField(null=False)
    type = models.CharField(max_length=20, choices=OptionChoices)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = 'quizzo'

    @classmethod
    def get_question_obj(cls, id):
        try:
            student_obj = cls.objects.get(id=id)
            return student_obj
        except cls.DoesNotExist:
            from rest_framework.exceptions import NotFound
            raise NotFound("Question not found")
