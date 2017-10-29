from __future__ import unicode_literals
from django.db import models
from .question import Question
from quizzo.models.quiz import Quiz
from quizzo.models.student import Student
from quizzo.models.student_quiz_attempt import StudentQuizAttempt


# Create your models here.
class StudentQuiz(models.Model):
    student = models.ForeignKey(Student)
    quiz = models.ForeignKey(Quiz)
    marks_obtained = models.IntegerField()
    grade = models.CharField(max_length=10)
    user_options = models.ManyToManyField(StudentQuizAttempt)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = 'quizzo'

    @classmethod
    def check_user_attempt(cls, username, quiz_id):
        from quizzo.models.student import Student
        student_obj = Student.get_student_obj(username)
        attempt = cls.objects.filter(student=student_obj, quiz_id=quiz_id)
        if attempt.count() > 0:
            return "true"
        else:
            return "false"
