from django.contrib import admin
from quizzo.models.question import Question
from quizzo.models.option import Option
from quizzo.models.student import Student
from quizzo.models.teacher import Teacher
from quizzo.models.student_quiz import StudentQuiz
from quizzo.models.student_quiz_attempt import StudentQuizAttempt
from quizzo.models.quiz import Quiz

# Register your models here.

admin.site.register(StudentQuizAttempt)
admin.site.register(StudentQuiz)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)

