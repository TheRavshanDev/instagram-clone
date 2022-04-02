from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from post.models import Media

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=55)
    bio = models.TextField(default=f"Hello! My name is {{name}}", max_length=400)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    photo = models.URLField(blank=True)
    date = models.DateField()
    followers = models.ManyToManyField(settings.ACC, on_delete=models.SET_NULL, null=True, blank=True)
    follows = models.ManyToManyField(settings.ACC, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def followers_number(self):
        return self.followers.count()

    def follows_number(self):
        return self.follows.count()

class Message(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField()
    to_whom = models.ForeignKey(Account, on_delete=models.CASCADE)
    from_whom = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(Account, on_delete=models.CASCADE,blank=True)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

