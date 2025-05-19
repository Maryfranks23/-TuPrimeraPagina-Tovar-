from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_recargas.urls')), # Incluimos las URLs de nuestra aplicación
]