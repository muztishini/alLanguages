from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers

# from lottee_new.helpers import get_object_or_none
from my_user.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from language.serializers import LanguageSerializer
# from otp.models import OTP


class UserSerializer(serializers.ModelSerializer):
    native = LanguageSerializer()
    learn = LanguageSerializer()
    old_password = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('balance',)
        extra_kwargs = {'password': {'write_only': True}, 'old_password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # get the hashed password
        instance = User.objects.create(**validated_data)  # create a user
        return instance

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'password' and check_password(validated_data['old_password'], instance.password):
                instance.password = make_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance


class UpdatePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)
    password_repeat = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError({'message': _('auth.password_mismatch')})
        user = self.context['request'].user
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({'message': _('auth.old_password_incorrect')})
        password_validation.validate_password(data['password'], user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['password']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=128, required=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)
    password_repeat = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError({'message': _('Passwords dismatch.')})
        return data

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data['password'])
        instance.save(update_fields=['password'])
        return instance
