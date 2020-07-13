from django.shortcuts import render
from .models import Book, Chapter
from .serializers import BookSerializer, ChapterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_chapter(request, number):
    if request.method == "GET":
        chapter = Chapter.objects.get(number=number)
        serializer = ChapterSerializer(chapter)
        return Response(serializer.data)

@api_view(['GET'])
def get_book(request, id):
    if request.method == "GET":
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)

        chapter_amount = len(book.chapter.all())
        new_serializer = {"chapter_amount":chapter_amount}
        new_serializer.update(serializer.data)

        return Response(new_serializer)



