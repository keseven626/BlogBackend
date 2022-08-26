from rest_framework import serializers
from .models import Post, Comment


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content','category','snippet','image','Allow_comment','Author', 'created', 'updated']

class CommentSerializer(serializers.ModelSerializer):
    comment_author  = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id','comment_author', 'post_comment', 'date_created', 'date_update', 'content']
    
class PostModelSerializer(serializers.ModelSerializer):
    Author_Name = serializers.CharField(source='Author.name')
    category = serializers.StringRelatedField(many=False )
    class Meta:
        model = Post
        ordering = ['created']
        fields = ['id', 
            'title', 'content','snippet','image','Author_id','Author_Name',
            'like','Allow_comment', 'created', 'updated', 'category', 'top_news']

