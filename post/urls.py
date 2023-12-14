from django.urls import path
from .views import PostViewSet,PostDetailView,PostPhotoDetailView

urlpatterns = [
    path('',PostViewSet.as_view(),name='postview'),
    path('<str:title>/', PostDetailView.as_view()),
    path('post-photo/<str:title>/', PostPhotoDetailView.as_view(), name='post-photo-detail'),
]
