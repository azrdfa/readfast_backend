from django.db import models
from django.utils import timezone

class Log(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"

    def __str__(self):
        localtime = timezone.localtime(self.timestamp)
        return f"{localtime}"