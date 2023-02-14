from django.db import models
from applications.post.models import Post
from django.contrib.auth import get_user_model


User = get_user_model()


class Like(models.Model):
    """
        Модель лайков
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    is_like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner} liked - {self.post.title}'