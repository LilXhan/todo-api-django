from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('api/v1/', include('tasks.urls')),
    path('api/v1/', include('tasks.urls')), 
    path('api/auth/', include('authapp.urls')),
    path(r'api/v2/', include('tasks_viewset.urls')),
    path(r'api/v1/', include('users.urls')),
    path('users/', include('usersjwt.urls'))
]
