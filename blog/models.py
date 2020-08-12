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



"""
The related_name argument is useful if you have more complex related class names. For example, if you have a foreign key 
relationship:

class UserMapDataFrame(models.Model):
    user = models.ForeignKey(User)

Now, in order to access UserMapDataFrame objects from the related User, the default call would be 
"User.usermapdataframe_set.all()", which it is quite difficult to read. Using the related_name 
allows you to specify a simpler or more legible name to get the reverse relation. 
In this case, if you specify user = models.ForeignKey(User, related_name='map_data'), 
the call would then be User.map_data.all().

related_name provides you an ability to let Django know how you are going to access Comment model from Post model 
or in general how you can access reverse models which is the whole point in creating ManyToMany fields 
and using ORM in that sense.
"""
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') #See the 56th line of 'post_detal' template.

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