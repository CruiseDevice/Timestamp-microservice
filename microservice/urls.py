from django.conf.urls import url

from .views import index, display, display1

app_name = 'microservice'

urlpatterns = [
    url(
        r'^$',
        index,
        name='index'
    )
]