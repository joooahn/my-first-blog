from django.db import models
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE);
    title = models.CharField(max_length=200)
    text = models.TextField()
    due_date = models.DateTimeField(default=timezone.now)
    priority = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# Create your models here.
