from rest_framework import serializers
from .models import CabUser

class UserSerializer(serializers.Serializer):
    """Serializer for CabUser model"""

    userName = serializers.CharField(max_length=124*4)
    lastName = serializers.CharField(max_length=248*4)
    emailAddress = serializers.EmailField(max_length=248*4)
    phoneNumber = serializers.CharField(max_length=19*4)
    hobbies = serializers.CharField(required=False, max_length=512*4, default="")
    validatedEmail = serializers.BooleanField(required=False, default=False)
    validatedNumber = serializers.BooleanField(required=False, default=False)


    def create(self, data):

        return CabUser.objects.create(**data)