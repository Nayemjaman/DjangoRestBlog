from django.contrib import admin
from .models import Post, Upvote, Comment

admin.site.register(Post)
admin.site.register(Upvote)
admin.site.register(Comment)