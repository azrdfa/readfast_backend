from django.urls import path
from .views import *

urlpatterns = [
    path("post-log/", post_log, name="post-log"),
    path("get-log/", get_log, name="get-log")
]
