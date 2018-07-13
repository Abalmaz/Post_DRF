from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Respons
from posts.permissions import IsOwnerOrReadOnly
from posts.models import Post, Category
from django.contrib.auth.models import User
from posts.serializers import PostSerializer, CategorySerializer, UserSerializer

# Create your views here.


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOr)

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostHighlight(generics.GenericAPIView):
    queryset = Post.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer, )


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

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Respons(post.highlighted)