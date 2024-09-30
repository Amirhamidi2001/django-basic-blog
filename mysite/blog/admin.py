from django.contrib import admin
from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):

    date_hierarchy = "created_at"
    list_display = ('title', 'author', 'created_at', 'status', 'published_at')
    list_filter = ('status', 'author', 'created_at', 'published_at')
    search_fields = ('title', 'content', 'author__username')
    # prepopulated_fields = {'slug': ('title',)}
    # fields = ('image', 'title', 'content', 'author', 'categories', 'tags', 'status', 'published_at', 'login_require')
    fields = ('image', 'title', 'content', 'author', 'categories', 'status', 'published_at', 'login_require')
    # filter_horizontal = ('categories', 'tags')
    filter_horizontal = ('categories',)
    empty_value_display = '-empty-'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
