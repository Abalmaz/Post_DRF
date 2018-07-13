from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from posts.models import Post, Category
from posts.serializers import PostSerializer, CategorySerializer

# Create your views here.

#
# def index(request):
#     return render(request, 'posts/index.html')


class PostsList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        # if self.action == 'create':
        #     return Create

        return self.serializer_class




