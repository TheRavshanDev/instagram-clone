from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=55)
    bio = models.TextField(default=f"Hello! My name is {{name}}", max_length=400)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    photo = models.URLField(blank=True)
    date = models.DateField()
    followers = models.ManyToManyField(settings.ACC, blank=True, related_name="user_followers")
    follows = models.ManyToManyField(settings.ACC, blank=True, related_name='user_follows')

    def __str__(self):
        return self.name

    def followers_number(self):
        return self.followers.count()

    def follows_number(self):
        return self.follows.count()

class Message(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account")
    text = models.TextField()
    to_whom = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="message_to_whom")
    from_whom = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="message_from_whom")
    date = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(Account, blank=True)
    media = models.ForeignKey(settings.MEDIA, on_delete=models.SET_NULL, null=True, blank=True)