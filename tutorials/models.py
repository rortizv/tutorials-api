from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=400,blank=False, default='')
    published = models.BooleanField(default=False)
