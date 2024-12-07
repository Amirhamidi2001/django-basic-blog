from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.contrib.auth.decorators import login_required


def blog_view(request, **kwargs):
    """
    Displays a paginated list of blog posts filtered by category, tag, date, or author.
    """
    posts = Post.objects.filter(status=1)

    if "cat_name" in kwargs:
        posts = posts.filter(category__name=kwargs["cat_name"])
    if "tag_name" in kwargs:
        posts = posts.filter(tags__name__in=[kwargs["tag_name"]])
    if "datetime" in kwargs:
        posts = posts.filter(published_at__date=kwargs["datetime"])
    if "author_username" in kwargs:
        posts = posts.filter(author__username=kwargs["author_username"])

    if not posts.exists():
        raise Http404("No posts match the given filters.")

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")

    try:
        page_number = int(page_number) if page_number else 1
        posts = paginator.page(page_number)
    except (ValueError, EmptyPage, PageNotAnInteger):
        posts = paginator.page(1)

    context = {"posts": posts}
    return render(request, "blog/blog.html", context)


@login_required
def single_view(request, pid):
    """
    Displays a single blog post with comments and allows authenticated users to submit new comments.
    """
    post = get_object_or_404(Post, pk=pid)
    post.counted_views += 1
    post.save()
    comments = post.comments.filter(approved=True)  # Only show approved comments
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()  # Save without approval
            return redirect("blog:single", pid=post.id)  # Redirect after submission

    context = {"post": post, "comments": comments, "comment_form": comment_form}
    return render(request, "blog/blog-single.html", context)


def blog_search(request):
    """
    Searches for blog posts containing the query string and displays the results.
    """
    posts = Post.objects.filter(status=1)
    query = request.GET.get("s", "")
    if query:
        posts = posts.filter(content__icontains=query)
    context = {"posts": posts, "query": query}
    return render(request, "blog/blog.html", context)
