from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post, Category


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts', 'is_staff')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description', 'is_active', 'user')
        model = Category


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ('id', 'status', 'category', 'user', 'title', 'content', 'created_on', 'updated_on')
