from rest_framework import serializers
from quiz.serializer_fields import JsonListField
from .models import File

class FileSerializer(serializers.ModelSerializer):
    extra_fields = JsonListField(required=False)

    class Meta:
        model = File
        fields = '__all__'