from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Item(models.Model):
    video = EmbedVideoField()
