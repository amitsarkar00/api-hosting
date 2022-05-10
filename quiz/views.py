from .models import Quiz
from rest_framework import viewsets, permissions , generics
from rest_framework.decorators import action
from .serializers import QuizSerializer #, QuizListSerializer
from rest_framework.response import Response


class QuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows quiz to be viewed or edited.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        topic = request.query_params.get('topic')
        
        if topic :
            queryset = Quiz.objects.filter(topic=topic)
        else:
            queryset = Quiz.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    # @action(detail=False, methods=['get','post'], serializer_class = QuizListSerializer)
    # def bulk_create(self, request):
    #     # self.serializer_class = QuizListSerializer
    #     queryset = self.get_queryset()
    #     print(queryset)
    #     serializer = QuizSerializer(queryset, many=True)
    #     return Response(serializer.data)

# class QuizListView(generics.CreateAPIView):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizListSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def create(self, request):
#         queryset = self.get_queryset()
#         print(queryset)
#         serializer = QuizListSerializer(queryset, many=True)
#         return Response(serializer.data)

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = QuizSerializer(queryset, many=True)
    #     return Response(serializer.data)