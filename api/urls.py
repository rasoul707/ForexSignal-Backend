"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import HttpResponse
from django.urls.conf import include
from django.urls import path
from django.conf import settings
from django.conf.urls import static
from django.views.static import serve


def HomeAPI(request): return HttpResponse("API")


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/', HomeAPI),
    path(r'api/auth/', include('authentication.urls')),
    path(r'api/setting/', include('appsetting.urls')),
    path(r'api/notice/', include('notice.urls')),
    path(r'api/upload/', include('upload.urls')),
    path(r'api/license/', include('license.urls')),
    path(r'api/news/', include('mynews.urls')),
    path(r'^media/(?P<path>.*)$', serve,
         {'document_root': settings.MEDIA_ROOT}),
    path(r'^static/(?P<path>.*)$', serve,
         {'document_root': settings.STATIC_ROOT}),
]
