from django.contrib.syndication.views import Feed
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog Latest Posts"
    link = "/rss/feed"
    description = "The blog latest posts"

    def items(self):
        return Post.objects.filter(status=True)[:5]

    def item_title(self, item):
        return item.title

    def item_content(self, item):
        return item.content[:100]
