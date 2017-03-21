from django.conf.urls import url
from django.views.generic import TemplateView

from guide import views
from guide import API_views


urlpatterns = [

    # Page urls
    url(r'^$',
        views.IndexView.as_view(),
        name='index',
        ),

    url(r'^a-propos/$',
        TemplateView.as_view(template_name="pages/about.html"),
        name='about',
        ),
    
    # API urls
    url(r'^api/guide/$', API_views.GuideAPIList.as_view()), 
    
]
