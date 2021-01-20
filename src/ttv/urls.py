from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from ttvdash.viewcontroller import(
    main
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('django.contrib.auth.urls')),
    path('', main.index, name='index'),
    path('login',main.login_view, name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
