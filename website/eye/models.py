from django.db import models

class Picture(models.Model):
    images = models.CharField(max_length = 200)