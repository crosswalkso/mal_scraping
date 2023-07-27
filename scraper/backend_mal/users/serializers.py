from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    mylist = serializers.SerializerMethodField()

    def get_mylist(self, user):
        return user.mylist()

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
            "mylist",
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


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"},
        write_only=True,
    )

    class Meta:
        model = User
        fields = (
            # "email",
            "username",
            "name",
            "password",
            "password2",
            "gender",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def save(self):
        user = User(
            # email=self.validated_data["email"],
            name=self.validated_data["name"],
            username=self.validated_data["username"],
            gender=self.validated_data["gender"],
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords musts match."})
        user.set_password(password)
        user.save()
        return user
