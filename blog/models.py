from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length = 500)
    image = models.ImageField(upload_to = 'uploads/',blank = True)
    date_posted = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.content

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.post.content, self.name)