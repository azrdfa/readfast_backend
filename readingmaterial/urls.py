from django.urls import path
from .views import get_book, get_chapter

app_name = "reregistration"
urlpatterns = [
    path("book", get_book, name="get-book"),
    path("chapter", get_chapter, name="get-chapter"),
]
