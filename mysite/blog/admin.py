from django.contrib import admin
from blog.models import Category, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):

    date_hierarchy = "created_at"
    list_display = ('title', 'author', 'created_at', 'status', 'published_at')
    list_filter = ('status', 'author', 'created_at', 'published_at')
    search_fields = ('title', 'content', 'author__username')
    # prepopulated_fields = {'slug': ('title',)}
    fields = ('image', 'title', 'content', 'author', 'category', 'tags', 'status', 'published_at', 'login_require')
    # filter_horizontal = ('category', 'tags')
    filter_horizontal = ('category',)
    empty_value_display = '-empty-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'approved', 'created_at')
    list_filter = ('approved',)
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
