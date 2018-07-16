from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post, Category


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'posts', 'is_staff',)


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(), write_only=True)
    author = UserSerializer(read_only=True, source='username')

    class Meta:
        fields = ('id', 'name', 'description', 'is_active', 'user', 'author',)
        model = Category


class PostSerializer(serializers.ModelSerializer):
    user_repr = serializers.HiddenField(default=serializers.CurrentUserDefault(), write_only=True)
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    status = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('url', 'id', 'status', 'category', 'user', 'user_repr', 'title', 'content', 'created_on',
                  'updated_on',)

    def get_status(self, obj):
        return obj.get_status_display()
