from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import SimpleRouter
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
]

urlpatterns = format_suffix_patterns(urlpatterns)