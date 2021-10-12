from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250)
    brief_description = models.CharField(max_length=250)
    full_description = models.CharField(max_length=350)
    image = models.URLField()
    posted = models.BooleanField(default=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.CharField(max_length=250)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    posted_com = models.BooleanField(default=False)

    def __str__(self):
        return self.text
