from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    url(r'^$', views.welcome, name = 'welcome'),
    url(r'^image/(?P<id>[\w-]+)$', views.image, name='image'),
    url(r'^allImages$',views.all_images,name='all_images'),
    url(r'^category/(?P<category>.+?)/$', views.category, name='category'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)