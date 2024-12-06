from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name = "blog"

urlpatterns = [
    path("", blog_view, name="blog"),
    path("<int:pid>/", single_view, name="single"),
    path("category/<str:cat_name>/", blog_view, name="category"),
    path("tag/<str:tag_name>/", blog_view, name="tag"),
    path("author/<str:author__username>/", blog_view, name="author"),
    path("date/<str:datetime>/", blog_view, name="date"),
    path("search/", blog_search, name="search"),
    path("rss/feed/", LatestEntriesFeed()),
]
