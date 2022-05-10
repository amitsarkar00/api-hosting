from rest_framework import serializers
from .serializer_fields import JsonListField
from .models import Quiz

# class QuizListSerializer(serializers.Serializer):
#     quizes = JsonListField()
#     # fields = []
#     def create(self, validated_data):
#         quizes = [Quiz(**item) for item in validated_data]
#         return Quiz.objects.bulk_create(quizes)

class QuizSerializer(serializers.ModelSerializer):
    answers = JsonListField()
    correct_answers = JsonListField()
    # answers = serializers.ListField(child=serializers.CharField())
    # correct_answers = serializers.ListField(child=serializers.CharField())

    # @classmethod
    # def many_init(cls, *args, **kwargs):
    #     # Instantiate the child serializer.
    #     kwargs['child'] = cls()
    #     # Instantiate the parent list serializer.
    #     return QuizListSerializer(*args, **kwargs)

    class Meta:
        model = Quiz
        fields = ['topic', 'question', 'answers', 'correct_answers']
        # list_serializer_class = QuizListSerializer


