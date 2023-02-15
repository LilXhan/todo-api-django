from rest_framework.viewsets import ModelViewSet
from rest_framework import status 
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .pagination import SimplePagination
from tasks.models import Todo
from .serializer import TodoSerializer

class TodoViewSetCustom(ModelViewSet):
    queryset = Todo.objects.all()
    pagination_class = SimplePagination

    def get_serializer(self, *args, **kwargs):
        return TodoSerializer

    def list(self, request):
        page = self.paginate_queryset(page, many=True)
        if page is not None:
            serializer = TodoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        if isinstance(request.data, list):
            serializer = TodoSerializer(data=request.data, many=True)
        else:
            serializer = TodoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(isntance=todo, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = get_object_or_404(todo, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        todo = get_object_or_404(Todo, pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




