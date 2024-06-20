from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from apps.core.views import ping

api = [
    path("ping/", ping),
    path("docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]

api_v1 = [
    path("", include("apps.users.urls", namespace="users")),
]


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/", include(api)),
    path("api/v1/", include(api_v1)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    if settings.ENABLE_DEBUG_TOOLBAR:
        urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
