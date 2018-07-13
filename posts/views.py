from rest_framework import generics
from posts.models import Post, Category
from django.contrib.auth.models import User
from posts.serializers import PostSerializer, CategorySerializer, UserSerializer

# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serialize_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serialize_class = UserSerializer