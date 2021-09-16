from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet, FollowViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='post_comments'
                )

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
