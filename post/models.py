from django.db import models
from member.models import Account

class Media(models.Model):
    photo = models.URLField(blank=True)
    video = models.URLField(blank=True)


class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField()
    media = models.ManyToManyField(Media, on_delete=models.CASCADE)
    location = models.CharField(max_length=150)
    tag = models.MaynToManyField(Account, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    #archived = models.

    def __str__(self):
        return self.date

class PostLikes(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Story(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    matn = models.TextField(blank=True,max_length=100)
    mention = models.ManyToManyField(Account, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.matn

class Highlight(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    story = models.ManyToManyField(Story, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    date = models.DateeTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class CommentLike(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
