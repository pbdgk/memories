from django.db import models
from django.conf import settings
from django.urls import reverse

import datetime


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.author.id, filename)


class Memory(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    media = models.FileField(upload_to=user_directory_path,
                             null=True,
                             blank=True)
    embed_id = models.CharField(max_length=50, default="", blank=True)
    created = models.DateTimeField()
    mime_type = models.CharField(max_length=30, default="")

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = datetime.datetime.now()
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('memories:detail',
                       kwargs={
                            'pk': self.pk,
                            'username': self.author.username})
    
    def __str__(self):
        return self.title

