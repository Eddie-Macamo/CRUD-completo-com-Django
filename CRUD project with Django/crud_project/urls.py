from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('membros.urls')),  # Substitua 'sua_app' pelo nome da sua aplicação
]
