from django.conf.urls import url
from django.urls import path,include

from .views import (
        exchange_dark
        )

app_name = 'exchange_app'
urlpatterns = [
    path('', exchange_dark, name='exchange_app_dark'),
]