from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Todo
from .serializers import TodoSerializer

class TaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
"""
    CRUD usando APIVIEW
"""

class TodoView(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({
            'ok': True,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'ok': True,
                'message': 'Todo created'
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'ok': False,
            'message': serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)

class TodoViewDetail(APIView):
    """Listar por id"""
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo)

        return Response({
            'ok': True,
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    """Actualizar por id"""
    def put(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(instance=todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'ok': True,
                'message': 'Todo updated'
            }, status=status.HTTP_200_OK)
        
        return Response({
            'ok': False,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    """ Eliminar por id"""
    def delete(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return Response({
            'ok': True,
            'message': 'Todo deleted'
        }, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({
                'ok': True,
                'message': 'Todo updated'
            }, status=status.HTTP_200_OK)

        return Response({
            'ok': False,
            'message': serializer.errors
        }, status=status.HTTP_502_BAD_GATEWAY)