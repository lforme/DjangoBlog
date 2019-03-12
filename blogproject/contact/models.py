from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField('最后修改日期', auto_now=True)


    def __str__(self):
        return self.subject


