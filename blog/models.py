from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(default=timezone.now())
    slug = models.SlugField(blank=True, editable = False)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()


    def get_absolute_url(self):
        return reverse("blog_list")

    def __str__(self):
        return self.title
