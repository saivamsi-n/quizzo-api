from rest_framework import serializers


class StudnetResponseType(object):
    def __init__(self, user_id, username, standard, **kwargs):
        self.id = user_id
        self.username = username
        self.standard = standard

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class StudentDetailsResponseSerializer(serializers.Serializer):
    username = serializers.CharField()
    id = serializers.IntegerField()
    standard = serializers.CharField()

    def create(self, validated_data):
        return StudnetResponseType(**validated_data)
