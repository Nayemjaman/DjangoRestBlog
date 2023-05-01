from django.contrib import admin
from .models import Post, Upvote, Comment


admin.site.register(Upvote)
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "title","created", "upvote_count")
    list_filter = ("user", "title","created")
    search_fields = ['title', 'user']