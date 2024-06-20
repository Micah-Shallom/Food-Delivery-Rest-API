from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password= serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationErrorError(detail="user with username exists")
        
        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationErrorError(detail="user with mail exists")
        
        phonenumber_exists = User.objects.filter(phone_number=attrs['phonenumber']).exists()

        if phonenumber_exists:
            raise serializers.ValidationErrorError(detail="user with phonenumber exists")
        
        return super().validate(attrs)