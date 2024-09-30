from django.db import models
from django.contrib.auth.models import User
# from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    # slug = models.SlugField(unique=True, max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=0)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='blog_posts')
    # tags = TaggableManager()
    counted_views = models.IntegerField(default=0)
    login_require = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
