from django.urls import path

from .views import index

app_name = 'microservice'

urlpatterns = [
    path(
        '',
        index,
        name='index'
    )
]