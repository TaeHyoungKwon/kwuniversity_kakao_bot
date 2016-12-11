from django.conf import settings
from django.db import models
from django.utils import timezone






class SearchWord(models.Model):
    word = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]












