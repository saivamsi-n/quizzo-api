from rest_framework import serializers


class ProfileType(object):
    def __init__(self, username, first_name, last_name, email, city, college, user_type, year=None, **kwargs):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.year = year
        self.college = college
        self.city = city
        self.user_type = user_type

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class ProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    college = serializers.CharField()
    year = serializers.CharField(required=False)
    email = serializers.CharField()
    city = serializers.CharField()
    user_type = serializers.CharField()

    def create(self, validated_data):
        return ProfileType(**validated_data)
