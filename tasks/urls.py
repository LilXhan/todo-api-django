from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('todo', views.TaskViewSet, basename='tasks')

urlpatterns = router.urls