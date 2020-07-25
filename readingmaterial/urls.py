from django.urls import path
from .views import *

urlpatterns = [
    path("all/", get_all, name="all"),
    path("story-content/<int:id>/", get_story_content, name="story-content"),
    path("book-chapters/<int:id>/", get_book_chapters, name="book-chapters"),
    path("chapter-content/<int:id>/", get_chapter_content, name="chapter-content"),
]
