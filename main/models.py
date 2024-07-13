from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TopBooks(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
