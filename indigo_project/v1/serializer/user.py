from rest_framework import serializers


class CreateUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, allow_null=False,
                                 allow_blank=False, required=True)
    phone_number = serializers.CharField(max_length=10, allow_null=False,
                                         allow_blank=False, required=True)
    email = serializers.CharField(max_length=255, allow_null=False,
                                  allow_blank=False, required=True)
