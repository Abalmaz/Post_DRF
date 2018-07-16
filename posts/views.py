from rest_framework import permissions, viewsets
from posts.permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly
from posts.models import Post, Category
from django.contrib.auth.models import User
from posts.serializers import PostSerializer, CategorySerializer, UserSerializer

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsStaffOrReadOnly, )


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
