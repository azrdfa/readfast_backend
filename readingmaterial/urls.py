from django.urls import path
from .views import get_book, get_chapter

app_name = "reregistration"
urlpatterns = [
    path("book/<int:id>", get_book, name="get-book"),
    path("chapter/<int:number>", get_chapter, name="get-chapter"),
]
