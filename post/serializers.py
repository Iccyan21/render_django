from rest_framework import serializers
from .models import Post,PostPhoto, PostMovie

class PostSerizliers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','photo','video']
        
#　動画のシリアライザー
class PostMovieSerializer(serializers.ModelSerializer):
    video = serializers.FileField(max_length=100)
    class Meta:
        model = PostMovie
        fields = ['title', 'video']
        
class PostPhotoSerializer(serializers.ModelSerializer):
    # Movie インスタンスの詳細データを含めることができる
    # many=True で複数のモデルをシリアライズできる
    # read_only=True で、このフィールドは読み取り専用になる
    movies = PostMovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = PostPhoto
        fields = ['title','photo','movies']
            
    
    