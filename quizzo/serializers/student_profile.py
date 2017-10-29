from rest_framework import serializers


class StudentProfileType(object):
    def __init__(self, username, first_name, last_name, email, password, standard, school, **kwargs):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.standard = standard
        self.school = school

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class StudentProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    school = serializers.CharField()
    standard = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        return StudentProfileType(**validated_data)
