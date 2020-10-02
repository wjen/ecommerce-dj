from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auctions/', include('auctions.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'))
]

urlpatterns += [
    path('', RedirectView.as_view(url='auctions/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)