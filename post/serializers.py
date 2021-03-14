from rest_framework import serializers

from .models import Like, Post


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("id", "user", "created_at")


class AnaliticSerializer(serializers.Serializer):
    day = serializers.DateTimeField()
    count = serializers.IntegerField()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "author", "created_at")

    def create(self, validated_data):
        validated_data["author"] = self.context.get("request").user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.edited = True
        return super().update(instance, validated_data)
