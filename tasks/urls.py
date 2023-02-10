# from rest_framework.routers import DefaultRouter
# from . import views
# router = DefaultRouter()
# router.register('todo', views.TaskViewSet, basename='tasks')
# urlpatterns = router.urls

from django.urls import path 
from . import views 

urlpatterns = [
    path('todo/', views.TodoView.as_view(), name='todo'),
    path('todo/<int:pk>/', views.TodoViewDetail.as_view(), name='todo_id')
]

