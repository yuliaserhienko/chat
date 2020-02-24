from django.contrib.auth.models import User
from django.db import models


class AuthorManager(models.Manager):
    def get_unauthenticated(self):
        return super().get_queryset().get_or_create(
            username='unauthenticated_user'
        )[0]


class Author(User):
    objects = AuthorManager()

    class Meta:
        proxy = True
        ordering = ('first_name', )


class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(max_length=256)
    text = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.author is None:
            self.author = Author.objects.get_unauthenticated()
        super().save(*args, **kwargs)
