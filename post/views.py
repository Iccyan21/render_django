from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions,views
from rest_framework import status
from .models import Post
from .serializers import PostSerizliers
from rest_framework import viewsets

class PostViewSet(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerizliers
    
class PostDetailView(generics.RetrieveAPIView):
    def get(self, request, title):
        try:
            post = Post.objects.get(title=title)
            serializer = PostSerizliers(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)