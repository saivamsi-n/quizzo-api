from django.conf.urls import include, url
from quizzo.views.student_signup.student_signup import student_signup
from quizzo.views.teacher_signup.teacher_signup import teacher_signup
from quizzo.views.student_login.student_login import student_login
from quizzo.views.teacher_login.teacher_login import teacher_login
from quizzo.views.get_next_quiz_details.get_next_quiz_details import next_quiz
from quizzo.views.get_students_list.get_students_list import get_student_list
from quizzo.views.check_student_quiz_attempt.check_student_quiz_attempt import check_student_quiz_attempt
from quizzo.views.student_quiz_list.student_quiz_list import get_student_quiz_list
from quizzo.views.get_quiz.get_quiz import get_quiz
from quizzo.views.get_leaderboard.get_leaderboard import get_leaderboard
from quizzo.views.quiz_attempt.quiz_attempt import quiz_answers
from quizzo.views.check_quizdate.check_quizdate import quizdate_attempt_check
from quizzo.views.check_quiz_present.check_quiz_present import check_quiz_present
from quizzo.views.quiz_statistics.quiz_statistics import quiz_statistics
from quizzo.views.get_user_info.get_user_info import get_user_info
from quizzo.views.update_student_profile.update_student_profile import update_student_profile
from quizzo.views.update_teacher_profile.update_teacher_profile import update_teacher_profile

urlpatterns = [
    url(r'^student/signup/$', student_signup, name="student_signup"),
    url(r'^teacher/signup/$', teacher_signup, name="teacher_signup"),
    url(r'^student/login/$', student_login, name="student_login"),
    url(r'^teacher/login/$', teacher_login, name="teacher_login"),
    url(r'^quiz/next/$', next_quiz, name="next_quiz"),
    url(r'^quiz/check/$', check_quiz_present, name='check_quiz'),
    url(r'^students/$', get_student_list, name="students_list"),
    url(r'^student/(?P<username>\w+)/quiz/(?P<quiz_id>\d+)/check/$', quizdate_attempt_check, name="quiz_date_check"),
    url(r'^student/(?P<username>\w+)/quiz/(?P<quiz_id>\d+)/$', check_student_quiz_attempt,
        name="student_quiz_attempt_check"),
    url(r'^student/(?P<username>\w+)/quizzes/$', get_student_quiz_list, name="student_quiz_list"),
    url(r'^student/(?P<username>\w+)/quiz/(?P<quiz_id>\d+)/test/$', get_quiz, name="get_quiz"),
    url(r'^leaderboard/$', get_leaderboard, name="get_leaderboard"),
    url(r'^student/(?P<username>\w+)/quiz/(?P<quiz_id>\d+)/answers/', quiz_answers, name='quiz_attempt'),
    url(r'^student/(?P<username>\w+)/quiz/reference/', quiz_statistics, name="quiz_statistics"),
    url(r'^profile/$', get_user_info, name='user_info'),
    url(r'^student/(?P<username>\w+)/profile/update/$', update_student_profile, name='student_profile_update'),
    url(r'^teacher/(?P<username>\w+)/profile/update/$', update_teacher_profile, name='teacher_profile_update'),
]
