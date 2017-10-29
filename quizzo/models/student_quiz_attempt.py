from __future__ import unicode_literals
from django.db import models
from .question import Question


# Create your models here.
class StudentQuizAttempt(models.Model):
    question = models.ForeignKey(Question)
    attempted_id = models.IntegerField(null=True)
    attempted_answer = models.CharField(max_length=300, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = 'quizzo'
