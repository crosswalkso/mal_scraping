from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "last_login",
            "username",
            "date_joined",
            "name",
            "is_manager",
            "avatar",
            "gender",
            "email",
        )


class MiniUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "is_manager",
            "avatar",
            "email",
        )
