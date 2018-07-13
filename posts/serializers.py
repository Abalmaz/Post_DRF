from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=20)
    # description = serializers.CharField(max_length=250)
    # is_active = serializers.BooleanField()
    # user = serializers.IntegerField(source='user_id')

    class Meta:
        fields = ('id', 'name', 'description', 'is_active', 'user')
        model = Category
        # read_only_fields = ('id', 'is_active')
        # extra_kwargs = {name:{}} передача дополнительных аргументов и полей


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    category_repr = CategorySerializer(read_only=True, source='category')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), write_only=True, slug_field='name')

    class Meta:
        model = Post
        fields = ('id', 'status', 'category_repr', 'category', 'user', 'title', 'content', 'created_on', 'updated_on')


    # id = serializers.IntegerField(read_only=True)
    # status = serializers.ChoiceField(required=False, choices=Post.STATUSES)
    # # category = serializers.IntegerField(source='category_id'
    # category = CategorySerializer(required=True)
    # user = serializers.IntegerField(required=False, source='user_id')
    # title = serializers.CharField(required=True, max_length=50)
    # content = serializers.CharField(required=True, max_length=250)
    # created_on = serializers.DateTimeField(read_only=True)
    # updated_on = serializers.DateTimeField(read_only=True)
    #
    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.category_id = validated_data['category']['id']
    #     instance.content = validated_data.get('content', instance.content)
    #     return instance

