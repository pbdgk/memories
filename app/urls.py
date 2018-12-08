from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticate/', include('authentication_app.urls')),
    path('memories/', include('memories.urls')),
    path('', RedirectView.as_view(url='memories/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
