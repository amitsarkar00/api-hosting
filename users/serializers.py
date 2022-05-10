from rest_framework import serializers
from users.models import Candidate, User
from users.helper import filter_dict

from quiz.serializer_fields import JsonListField
from companies.serializers import AdminSerializer, HrSerializer

class UserSerializer(serializers.ModelSerializer):
    extra_fields = JsonListField(allow_null=True, required=False)

    class Meta:
        model = User
        # fields = ['first_name', 'last_name', 'username', 'email', 'password']
        exclude = ['token', 'is_active', 'is_admin', 'last_login']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'role' : {'read_only': True},
            'auth_provider' : {'read_only': True},
        }
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        if(validated_data.get('password')):
            instance.set_password(validated_data['password'])
            validated_data.pop('password')
        for field in validated_data.keys():
            if(hasattr(instance, field)):
                setattr(instance, field, validated_data[field])
        instance.save()
        return instance

class CandidateSerializer(serializers.ModelSerializer):
    skills = JsonListField(required=False, allow_null=True, default=None)
    address = JsonListField(required=False, allow_null=True, default=None)
    extra_fields = JsonListField(required=False, allow_null=True, default=None)
    user = UserSerializer(required=False)

    class Meta:
        model = Candidate
        fields = '__all__'
        depth = 0

class CandidateUserSerializer(UserSerializer):
    candidate = CandidateSerializer(read_only=True)

class HrUserSerializer(UserSerializer):
    hr = HrSerializer(read_only=True)

class AdminUserSerializer(UserSerializer):
    admin = AdminSerializer(read_only=True)