from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'posts', 'is_staff')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description', 'is_active', 'user')
        model = Category


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='post-highlight', format='html')

    class Meta:
        model = Post
        fields = ('url', 'id', 'status', 'category', 'highlight', 'user', 'title', 'content', 'created_on', 'updated_on')
