from rest_framework.routers import DefaultRouter

from .routers import CustomRouter
from .api import UserViewSet, UserViewGenericViewSet

router = DefaultRouter()

custom_router = CustomRouter()

router.register(r'users', UserViewSet, basename='users')
custom_router.register(r'custom/users', UserViewGenericViewSet, basename='users_custom')

urlpatterns = router.urls 
urlpatterns += custom_router.urls