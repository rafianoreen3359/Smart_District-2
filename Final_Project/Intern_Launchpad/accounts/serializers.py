from rest_framework import serializers
from django.contrib.auth.models import User
from .models import InternProfile


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    full_name = serializers.CharField()
    department = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'full_name',
            'department'
        ]

    def create(self, validated_data):

        full_name = validated_data.pop('full_name')
        department = validated_data.pop('department')

        user = User.objects.create_user(
            **validated_data
        )

        InternProfile.objects.create(
            user=user,
            full_name=full_name,
            department=department
        )

        return user


class ProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source='user.username',
        read_only=True
    )

    email = serializers.EmailField(
        source='user.email',
        read_only=True
    )

    class Meta:
        model = InternProfile
        fields = [
            'id',
            'username',
            'email',
            'full_name',
            'phone',
            'department',
            'skills',
            'bio'
        ]