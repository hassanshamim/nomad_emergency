"""emergency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.urls import path, re_path
from django.contrib.gis import admin

from maps import views as map_views

urlpatterns = [
    # TODO: switch to path() and re_path ()
    url(r'^admin/', admin.site.urls),
    url(r'^map/', map_views.index, name='map'),
    url(r'^$', map_views.index, name='home'),
    url(r'^facility/(?P<facility_id>[0-9]+)', map_views.show_facility, name='facility'),
    url(r'^facility/new', map_views.new_facility, name='new'),
    path('pages/', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))