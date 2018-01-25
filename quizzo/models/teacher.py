from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from rest_framework.exceptions import NotFound, AuthenticationFailed, ParseError


# Create your models here.


class Teacher(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    college = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = 'quizzo'

    @classmethod
    def sign_up(cls, request_data):
        from quizzo.utils.user_check import check_username_present
        check_username_present(request_data.username)

        try:
            from django.db import transaction
            with transaction.atomic():
                user_obj = User.objects.create_user(username=request_data.username,
                                                    password=request_data.password)

                teacher_obj = cls.objects.create(
                    user=user_obj,
                    username=request_data.username,
                    email=request_data.email,
                    first_name=request_data.first_name,
                    last_name=request_data.last_name,
                    college=request_data.college
                )
        except Exception as e:
            raise e
        return teacher_obj

    @classmethod
    def login(cls, request_obj):
        try:
            user = User.objects.get(username=request_obj.username)
            if user.check_password(request_obj.password):
                user = user
                return cls.objects.get(user=user)
        except User.DoesNotExist:
            raise AuthenticationFailed("Username or password is incorrect")

    @classmethod
    def get_teacher_details(cls, id):
        try:
            teacher_obj = cls.objects.get(id=id)
            obj = {
                "username": teacher_obj.username,
                "college": teacher_obj.college,
                "first_name": teacher_obj.first_name,
                "last_name": teacher_obj.last_name,
                "city": teacher_obj.city,
                "email": teacher_obj.email,
                "user_type": "teacher"
            }
            return obj
        except cls.DoesNotExist:
            raise NotFound("Student not found")

    @classmethod
    def update_profile(cls, request_data, username):
        try:
            from django.db import transaction
            with transaction.atomic():

                from django.contrib.auth.models import User
                user_obj = User.objects.get(username=username)
                user_obj.set_password(request_data.password)
                user_obj.save()
                teacher_obj = cls.objects.get(user=user_obj)
                if teacher_obj.username != request_data.username:
                    from quizzo.utils.user_check import check_username_present
                    check_username_present(request_data.username)
                teacher_obj.user = user_obj
                teacher_obj.username = request_data.username
                teacher_obj.email = request_data.email
                teacher_obj.first_name = request_data.first_name
                teacher_obj.last_name = request_data.last_name
                teacher_obj.standard = request_data.standard
                teacher_obj.college = request_data.college
                teacher_obj.save()
                return teacher_obj
        except:
            raise ParseError("Teacher Profile cannot be Updated")
