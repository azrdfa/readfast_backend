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
            chapter_amount = len(book.chapter.all())
            book_dict = {"chapter_amount": chapter_amount}
            serializer = BookSerializer(book)
            book_dict.update(serializer.data)
            book_serializer.append(book_dict)

        return Response(book_serializer)

@api_view(['GET'])
def get_chapter(request, number):
    if request.method == "GET":
        chapter = Chapter.objects.get(number=number)
        serializer = ChapterSerializer(chapter)
        return Response(serializer.data)




