from rest_framework.routers import DefaultRouter
from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


from . import api

router = DefaultRouter()

router.register('', api.GetUsers, basename='getUsers')

urlpatterns = [
    path('singup/', api.SignUpView.as_view(), name='singup'),
    path('login/', api.LoginView.as_view(), name='login'),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify')
]


urlpatterns += router.urls

