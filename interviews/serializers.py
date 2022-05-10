from rest_framework import serializers
from quiz.serializer_fields import JsonListField
from .models import Interview

class InterviewSerializer(serializers.ModelSerializer):
    extra_fields = JsonListField()

    class Meta:
        model = Interview
        fields = '__all__'