from rest_framework import serializers
from .models import Post

class PostSerizliers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','photo','video']