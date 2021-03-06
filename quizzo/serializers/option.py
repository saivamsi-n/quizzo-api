from rest_framework import serializers


class OptionType(object):
    def __init__(self, option=None, option_id=None, **kwargs):
        self.option = option
        self.option_id = option_id

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class OptionSerializer(serializers.Serializer):
    option_id = serializers.IntegerField(default=20)
    option = serializers.CharField()

    def create(self, validated_data):
        return OptionType(**validated_data)
