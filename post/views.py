from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions,views
from rest_framework import status
from .models import Post,PostPhoto
from .serializers import PostSerizliers,PostPhotoSerializer
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
        
class PostPhotoDetailView(APIView):
    def get(self, request, title):
        try:
            post_photo = PostPhoto.objects.get(title=title)
            serializer = PostPhotoSerializer(post_photo)
            return Response(serializer.data)
        except PostPhoto.DoesNotExist:
            return Response({'message': 'Photo not found'}, status=status.HTTP_404_NOT_FOUND)