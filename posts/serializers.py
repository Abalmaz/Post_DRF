from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post, Category


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description', 'is_active', 'user')
        model = Category



class PostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Post
        fields = ('id', 'status', 'category_repr', 'category', 'user', 'title', 'content', 'created_on', 'updated_on')
