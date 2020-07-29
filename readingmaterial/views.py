from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(["GET"])
def get_all(request):
    if request.method == "GET":
        reading_materials = { "data" : list() }
        books = Book.objects.values("id", "title", "sub_title", "author", "language").order_by("title")
        stories = Story.objects.values("id", "title", "sub_title", "author", "language").order_by("title")
        for book in books:
            tags = Book.objects.get(id=book["id"]).tag_set.values_list("name", flat=True)
            book["tags"] = list(tags)
            book["category"] = "book"
            reading_materials["data"].append(book)
        for story in stories:
            tags = Story.objects.get(id=story["id"]).tag_set.values_list("name", flat=True)
            story["tags"] = list(tags)
            story["category"] = "story"
            reading_materials["data"].append(story)
        return JsonResponse(reading_materials)

@api_view(["GET"])
def get_story_content(request, id):
    if request.method == "GET":
        content = { "data": "" }
        story = Story.objects.get(id=id)
        content["data"] = story.content
        return JsonResponse(content)

@api_view(["GET"])
def get_book_chapters(request, id):
    if request.method == "GET":
        chapters = { "data": "" }
        book = Book.objects.get(id=id)
        chapters["data"] = list(book.chapter.values("id", "title", "number").order_by("number"))
        return JsonResponse(chapters)

@api_view(["GET"])
def get_chapter_content(request, id):
    if request.method == "GET":
        content = { "data": "" }
        chapter = Chapter.objects.get(id=id)
        content["data"] = chapter.content
        return JsonResponse(content)