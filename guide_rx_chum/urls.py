from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from guide_rx_chum import settings

urlpatterns = [

    # App urls
    url(r'^filer/', include('filer.urls')),

    url(r'^admin/', admin.site.urls),
    
    url(r'^', include('guide.urls')),

    # Django REST framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
