from django.db import models


class Chat(models.Model):
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
