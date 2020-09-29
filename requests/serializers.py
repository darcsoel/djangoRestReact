from rest_framework import serializers

from requests.models import Request


class RequestSerializer(serializers.ModelSerializer):
    type = serializers.CharField(required=True)
    text = serializers.CharField(required=True)
    price = serializers.DecimalField(required=False, min_value=1, max_value=10000, decimal_places=2, max_digits=9)
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
        fields = ('user', 'type', 'user_info', 'text', 'price')
