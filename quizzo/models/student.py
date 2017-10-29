from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from rest_framework.exceptions import NotFound, AuthenticationFailed, ParseError


# Create your models here.


class Student(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    standard = models.IntegerField()
    school = models.CharField(max_length=100)
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
                from django.contrib.auth.models import User
                user_obj = User.objects.create_user(username=request_data.username,
                                                    password=request_data.password)

                student_obj = cls.objects.create(
                    user=user_obj,
                    username=request_data.username,
                    email=request_data.email,
                    first_name=request_data.first_name,
                    last_name=request_data.last_name,
                    standard=request_data.standard,
                    school=request_data.school
                )
        except:
            raise ParseError("Student cannot be registered")
        return student_obj

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
    def get_student_obj(cls, username):
        try:
            student_obj = cls.objects.get(username=username)
            return student_obj
        except cls.DoesNotExist:
            raise NotFound("Student not found")

    @classmethod
    def get_student_details(cls, id):
        try:
            student_obj = cls.objects.get(id=id)
            obj = {
                "username": student_obj.username,
                "school": student_obj.school,
                "standard": student_obj.standard,
                "first_name": student_obj.first_name,
                "last_name": student_obj.last_name,
                "city": student_obj.city,
                "email": student_obj.email,
                "user_type": "student"
            }
            return obj
        except cls.DoesNotExist:
            raise NotFound("Student not found")

    @classmethod
    def update_profile(cls, request_data,username):
        try:
            from django.db import transaction
            with transaction.atomic():

                from django.contrib.auth.models import User
                user_obj = User.objects.get(username=username)
                user_obj.set_password(request_data.password)
                user_obj.save()
                student_obj = cls.objects.get(user=user_obj)
                if student_obj.username != request_data.username:
                    from quizzo.utils.user_check import check_username_present
                    check_username_present(request_data.username)
                student_obj.user=user_obj
                student_obj.username=request_data.username
                student_obj.email=request_data.email
                student_obj.first_name=request_data.first_name
                student_obj.last_name=request_data.last_name
                student_obj.standard=request_data.standard
                student_obj.school=request_data.school
                student_obj.save()
                return student_obj
        except:
            raise ParseError("Student Profile cannot be Updated")
