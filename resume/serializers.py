from rest_framework import serializers
from quiz.serializer_fields import JsonListField
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    data = JsonListField()

    class Meta:
        model = Resume
        fields = '__all__'