from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),  # dashboard 앱의 URLConf 포함
]

if settings.DEBUG:  # DEBUG 모드에서만 활성화
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)