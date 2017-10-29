def create_student(username):
    from quizzo.models.student import Student
    from django.contrib.auth.models import User
    user = User.objects.create(
        username=username, email='test@gmail.com', password='top_secret123')
    student_obj = Student.objects.create(user=user, username=username, city="hyd", school="test school",
                                         standard=10, email="test@gmail.com", first_name="first_test",
                                         last_name="last_test")
    return student_obj

def create_teacher(username):
    from quizzo.models.teacher import Teacher
    from django.contrib.auth.models import User
    user = User.objects.create(
        username=username, email='test@gmail.com', password='top_secret123')
    teacher_obj = Teacher.objects.create(user=user, username=username, city="hyd", school="test school",
                                         email="test@gmail.com", first_name="first_test",
                                         last_name="last_test")
    return teacher_obj


def create_quiz(title):
    from quizzo.models.quiz import Quiz
    from datetime import datetime
    quiz_obj = Quiz.objects.create(title=title, description="testdescription", time=datetime.now())
    return quiz_obj


def create_studentquiz(student_obj, quiz_obj):
    from quizzo.models.student_quiz import StudentQuiz
    student_quiz_obj = StudentQuiz.objects.create(quiz=quiz_obj, student=student_obj, marks_obtained=50, grade="c")
    return student_quiz_obj


def create_questions():
    from quizzo.models.question import Question
    question_obj = Question.objects.create(question_content="value of pi?", marks=10, answer_id=1, type="mcq")
    from quizzo.models.option import Option
    option1 = Option.objects.create(content="3.14")
    option2 = Option.objects.create(content="3.33")
    option3 = Option.objects.create(content="3.89")
    question_obj.options.add(option1, option2, option3)
    question_obj.save()
    return question_obj
