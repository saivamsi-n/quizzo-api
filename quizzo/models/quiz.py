from __future__ import unicode_literals
from django.db import models
from .question import Question
from rest_framework.exceptions import NotFound


class Quiz(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)
    time = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = 'quizzo'

    @classmethod
    def get_next_quiz(cls):
        try:
            next_quiz = cls.objects.order_by('time').reverse()[0]
            if next_quiz is not None:
                return next_quiz
            else:
                raise NotFound("No Quiz available")
        except:
            raise NotFound("No Quiz avaialable")

    @classmethod
    def check_quiz_present(cls):
        quiz_obj = Quiz.objects.filter()
        if quiz_obj.count() > 0:
            return "true"
        else:
            return "false"

    @classmethod
    def get_quiz_obj(cls, id):
        try:
            quiz_obj = Quiz.objects.get(id=id)
            return quiz_obj
        except cls.DoesNotExist:
            NotFound("Quiz with specific id not found")
