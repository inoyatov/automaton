from django.urls import path
from .views import push_notifications

app_name = 'repositories'

urlpatterns = [
    path(
        '<str:repository_name>',
        push_notifications,
    ),
]
