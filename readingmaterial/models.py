from django.db import models

class Book(models.Model):

    title = models.CharField(
        blank=False,
        max_length=50,
        verbose_name="title"
        )
    sub_title = models.CharField(
        blank=False,
        max_length=50,
        verbose_name="sub_title"
        )
    author = models.CharField(
        blank=False,
        max_length=50,
        verbose_name="author"
        )
    language = models.CharField(
        blank=False,
        max_length=50,
        verbose_name="language"
    )

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.title} {self.sub_title} by {self.author}"

class Chapter(models.Model):

    title = models.CharField(
        blank=False, 
        max_length=50)
    number = models.IntegerField(
        blank=False,
        verbose_name="number")
    book = models.ForeignKey(
        blank=False,
        to=Book, 
        on_delete=models.CASCADE,
        related_name="chapter",
        verbose_name="book")
    content = models.TextField(
        blank=False,
        verbose_name="content"
        )

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"

    def __str__(self):
        return f"{self.book.title} {self.book.sub_title} chapter {self.number}"

class Story(models.Model):

    title = models.CharField(
        blank=False,
        max_length=50,
        verbose_name="title"
        )
    sub_title = models.CharField(
        blank=False,
        max_length=50,
        verbose_name="sub_title"
        )
    author = models.CharField(
        blank=False,
        max_length=50,
        verbose_name="author"
        )
    language = models.CharField(
        blank=False,
        max_length=50,
        verbose_name="language"
    )
    content = models.TextField(
        blank=False,
        verbose_name="content"
    )

    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"

    def __str__(self):
        return f"{self.title} {self.sub_title} by {self.author}"