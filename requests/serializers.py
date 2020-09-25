from rest_framework import serializers

from requests.models import Request


class RequestSerializer(serializers.ModelSerializer):
    type = serializers.CharField(required=True)
    user = serializers.IntegerField(required=False, write_only=True)
    user_info = serializers.CharField(read_only=True)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def to_representation(self, instance):
        instance.user_info = instance.user
        return super().to_representation(instance)

    class Meta:
        model = Request
        fields = ('user', 'type', 'user_info')
