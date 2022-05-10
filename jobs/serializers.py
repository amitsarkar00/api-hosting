from rest_framework import serializers
from quiz.serializer_fields import JsonListField
from users.serializers import UserSerializer
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    extra_fields = JsonListField(required=False, allow_null=True)
    posted_by = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
        depth = 0
    
    def create(self, validated_data):
        hr_user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            hr_user = request.user
        job = Job.objects.create(**validated_data, posted_by=hr_user)
        return job