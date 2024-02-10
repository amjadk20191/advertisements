
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/Chat/', include('Chat.urls')),
    path('api/advertiser/', include('advertiser.urls')),
    path('api/user/', include('user.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('payment/', include('payment.urls')),
    path('api/', include('core.urls')),


]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

