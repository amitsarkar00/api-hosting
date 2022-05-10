from rest_framework import serializers
from quiz.serializer_fields import JsonListField
from .models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    extra_fields = JsonListField(required=False, allow_null=True, default=None)

    class Meta:
        model = Meeting
        fields = '__all__'