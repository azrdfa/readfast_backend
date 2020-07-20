from django.shortcuts import render
from .models import Book, Chapter
from .serializers import BookSerializer, ChapterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_book(request):
    if request.method == "GET":
        books = Book.objects.all()

        book_serializer = list()
        # get book amount of chapter
        for book in books:
            chapters = book.chapter.all()
            chapter_list = list()
            for chapter in chapters:
                chapter_list.append({ "id": chapter.id, "number" : chapter.number, "title" : chapter.title })
            book_dict = {"chapters": chapter_list}
            serializer = BookSerializer(book)
            book_dict.update(serializer.data)
            book_serializer.append(book_dict)

        return Response(book_serializer)

@api_view(['GET'])
def get_chapter(request, chapter_id):
    if request.method == "GET":
        chapter = Chapter.objects.get(id=chapter_id)
        serializer = ChapterSerializer(chapter)
        return Response(serializer.data)