from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User #장고 기본 모델 불러오기

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
        