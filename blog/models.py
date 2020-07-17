from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Each model maps to a single database table.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=150, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.slug})



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return '{} by {}'.format(self.text, self.name)


# The migrate command actually applies the migrations to your database.
# আর makemigrations command টি migrations create করে ।

"""
Database migrations kebol field er khetre projujjo. tai field e kuno change anle shekhetre 
remigration kore nite hobe development server theke. onnothay kuno new method jug korar khetre
kebol file tike save dewai enough.
"""