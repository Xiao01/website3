from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Articles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="articles_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title