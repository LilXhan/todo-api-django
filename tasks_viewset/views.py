from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from tasks.models import Todo
from tasks.serializers import TodoSerializer
from .pagination import SimplePagination

# GET, RETRIEVE
class TaskReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = SimplePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('title', 'body')
    search_fields = ('title', 'body')


# GET, POST, PUT, PATCH, RETRIEVE, DELETE
class TaskViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = SimplePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'body')


