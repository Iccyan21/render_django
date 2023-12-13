from django.urls import path
from .views import PostViewSet,PostDetailView

urlpatterns = [
    path('',PostViewSet.as_view(),name='postview'),
    path('<str:title>/', PostDetailView.as_view()),
]
