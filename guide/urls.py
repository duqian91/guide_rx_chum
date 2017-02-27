from django.conf.urls import url
from django.views.generic import TemplateView

from guide import views
from guide import API_views


urlpatterns = [

    # API urls
    url(r'^api/guide/$', API_views.GuideAPIList.as_view()),
]
