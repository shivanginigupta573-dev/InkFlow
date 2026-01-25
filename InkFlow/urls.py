from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Connects your 'posts' app URLs
    path('', include('posts.urls')),
    
    path("__reload__/", include("django_browser_reload.urls")),

    # Connects Django's built-in login/logout system
    path('accounts/', include('django.contrib.auth.urls')),
]

# This allows the browser to see the photos you upload in VS Code
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)