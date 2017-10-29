from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Option(models.Model):
    content = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = 'quizzo'
