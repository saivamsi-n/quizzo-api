from rest_framework import serializers


class TeacherProfileType(object):
    def __init__(self, username, first_name, last_name, email, password, college, **kwargs):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.college = college

    def __unicode__(self):
        return str(self)

    # def __str__(self):
    #     return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class TeacherProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    college = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        return TeacherProfileType(**validated_data)
