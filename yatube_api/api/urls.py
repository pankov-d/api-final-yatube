from django.urls import path, include
from rest_framework import routers

import api.views as api_views

v1_router = routers.DefaultRouter()
v1_router.register('posts', api_views.PostViewSet)
v1_router.register('groups', api_views.GroupViewSet)
v1_router.register(r'^posts/(?P<post_id>\d+)/comments',
                   api_views.CommentViewSet,
                   basename='comments')
v1_router.register('follow', api_views.FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
