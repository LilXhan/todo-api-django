from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, TaskReadOnlyViewSet

task_router = DefaultRouter()

task_router.register(r'todo', TaskViewSet, basename='todo_model_viewset')
task_router.register(r'todo', TaskReadOnlyViewSet, basename='todo_read_only_model_viewset')

urlpatterns = task_router.urls
