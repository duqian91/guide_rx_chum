from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # App urls
    url(r'^', include('guide.urls')),
    url(r'^filer/', include('filer.urls')),

    # Django REST framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
