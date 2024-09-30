from django.contrib import admin
from website.models import Contact


class ContactAdmin(admin.ModelAdmin):

    date_hierarchy = "created_at"
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at', "email")
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Contact, ContactAdmin)
