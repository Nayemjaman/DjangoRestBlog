from rest_framework import serializers
from .models import Post,Upvote,Comment

class PostSerializer(serializers.ModelSerializer):
    user = seializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created', 'updated', 'user', 'upvote_count')

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = ('id', 'post', 'user')

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ('id', 'post', 'body','user')
