from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class AboutmeInfo(models.Model):

    text = models.TextField()
    weibo = models.URLField()
    github = models.URLField()
    twitter = models.URLField(default='')

    def __str__(self):

        return self.text

