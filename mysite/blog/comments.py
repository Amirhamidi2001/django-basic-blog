How to add the ability to leave comments for posts by users visiting the blog?
Note: To display the comments, the superuser must first approve it
Note: Use the forms.py
# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True)

# views.py
from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, "blog/blog.html", context)

def single_view(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {"post": post}
    return render(request, "blog/blog-single.html", context)

# urls.py
from django.urls import path
from blog.views import *

app_name = "blog"

urlpatterns = [
    path("", blog_view, name="blog"),
    path("<int:pid>/", single_view, name="single"),
]

# html
<div class="reply-form">
  <h4>Leave a Reply
  </h4>
  <p>Your email address will not be published. Required fields are marked * 
  </p>
  <form action="">
    <div class="row">
      <div class="col-md-6 form-group">
        <input name="name" type="text" class="form-control" placeholder="Your Name*">
      </div>
      <div class="col-md-6 form-group">
        <input name="email" type="text" class="form-control" placeholder="Your Email*">
      </div>
    </div>
    <div class="row">
      <div class="col form-group">
        <input name="website" type="text" class="form-control" placeholder="Your Website">
      </div>
    </div>
    <div class="row">
      <div class="col form-group">
        <textarea name="comment" class="form-control" placeholder="Your Comment*"></textarea>
      </div>
    </div>
    <button type="submit" class="btn btn-primary">Post Comment</button>
  </form>
</div>