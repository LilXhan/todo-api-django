from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from .models import JWTUser

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = JWTUser 
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email_exists = JWTUser.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError('This email has already been used')
        
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)

        return user


class GetUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = JWTUser
        fields = ['email', 'username', 'password', 'created_at']
