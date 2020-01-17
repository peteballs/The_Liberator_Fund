from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('static_web_pages.urls')),
    path('admin/', admin.site.urls),
    
]
