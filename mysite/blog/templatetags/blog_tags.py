from django import template
from blog.models import Post, Category
from django.db.models import Count, Q

register = template.Library()


@register.filter
def snippet(value, length=100):
    """Truncate the given value to the specified length."""
    if not isinstance(value, str):
        return value  # Return the original value if it's not a string
    return value[:length] + ("..." if len(value) > length else "")


@register.inclusion_tag("blog/blog-recent-posts.html")
def show_recent_posts(count=3):
    recent_posts = Post.objects.filter(status=1).order_by("-published_at")[:count]
    # return posts
    return {"recent_posts": recent_posts}


@register.inclusion_tag("blog/blog-categories.html")
def categories():
    # Get categories with the count of published posts
    categories_with_counts = Category.objects.annotate(
        post_count=Count("post", filter=Q(post__status=1))
    )
    return {"categories": categories_with_counts}
