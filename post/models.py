from django.db import models
from member.models import Account
from django.conf import settings

class Media(models.Model):
    photo = models.URLField(blank=True)
    video = models.URLField(blank=True)


class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField()
    media = models.ManyToManyField(Media)
    location = models.CharField(max_length=150)
    tag = models.ManyToManyField(Account, related_name="tags")
    date = models.DateTimeField(auto_now_add=True)
    archived = models.ManyToManyField(settings.ARCHIVED_POSTS)

    def __str__(self):
        return self.date

class PostLikes(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Story(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    description = models.TextField(blank=True,max_length=100)
    mention = models.ManyToManyField(Account, related_name="mention")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Highlight(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    story = models.ManyToManyField(Story)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class CommentLike(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
