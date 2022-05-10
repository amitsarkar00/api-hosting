from rest_framework import serializers
from quiz.serializer_fields import JsonListField
from .models import Admin, Company, Hr

class CompanySerializer(serializers.ModelSerializer):
    extra_fields = JsonListField(required=False, allow_null=True)

    class Meta:
        model = Company
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class HrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hr
        fields = '__all__'