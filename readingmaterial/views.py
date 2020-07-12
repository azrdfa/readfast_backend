from django.shortcuts import render
from .models import Book, Chapter
from .serializers import BookSerializer, ChapterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_chapter(request):
    if request.method == "GET":
        chapters = Chapter.objects.all()
        serializer = ChapterSerializer(chapters, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_book(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)



