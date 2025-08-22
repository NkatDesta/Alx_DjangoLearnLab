from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following", blank=True)

    def follow(self, user):
        """Follow another user"""
        if user != self:
            self.followers.add(user)

    def unfollow(self, user):
        """Unfollow a user"""
        if user != self:
            self.followers.remove(user)

    def is_following(self, user):
        return self.followers.filter(id=user.id).exists()

    def __str__(self):
        return self.username
