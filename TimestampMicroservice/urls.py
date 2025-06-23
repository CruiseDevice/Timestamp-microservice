"""TimestampMicroservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib import admin

from microservice.views import display, display1, timestamp_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('microservice.urls')),
    # New unified timestamp API endpoint
    re_path(
        r'^api/timestamp/(?P<timestamp_input>.*)/$',
        timestamp_api,
        name='timestamp_api'
    ),
    re_path(
        r'^(?P<month>\d{2})-(?P<day>\d{2})-(?P<year>\d{4})/$',
        display,
        name='display'
    ),
    re_path(
        r'^(?P<id>[0-9]+)/$',
        display1,
        name='display1'
    )
]
