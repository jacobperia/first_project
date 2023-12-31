from django.db import models

# Create your models here.
class UrlLink(models.Model):
    original_url = models.URLField(max_length=200)

    def __str__(self):
        return self.original_url