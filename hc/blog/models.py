from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class BlogCategory(models.Model):
    title=models.CharField(max_length=300)


    def __str__(self):
        return self.title


class BlogPost(models.Model):
    author = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=300, blank = False)
    content = HTMLField()
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog posts"

    def __str__(self):
        return self.title        
