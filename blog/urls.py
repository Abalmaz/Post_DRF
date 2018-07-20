"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from posts import views

schema_view = get_swagger_view(title='Posts API')

router = SimpleRouter()
router.register(r'post', views.PostViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    url(r'^$', views.index),
    url(r'^schema', schema_view),
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),

]

urlpatterns = format_suffix_patterns(urlpatterns)

