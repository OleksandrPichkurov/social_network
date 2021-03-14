from django.db.models import Count
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import Like, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import AnaliticSerializer, LikeSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Viewset for Post model
    """

    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(
        methods=["POST"],
        detail=True,
        permission_classes=[permissions.IsAuthenticated],
        url_path="like",
        url_name="like",
    )
    def like(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound({"post": "does not exist"})
        like = post.like_post(user_id=request.user.id)
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(
        methods=["PATCH"],
        detail=True,
        permission_classes=[permissions.IsAuthenticated],
        url_path="unlike",
        url_name="unlike",
    )
    def unlike(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound({"post": "does not exist"})
        post.unlike_post(user_id=request.user.id)
        return Response(status=status.HTTP_200_OK)


class AnaliticsLikeListView(generics.ListAPIView):
    """
    API View List of Likes of a specified date range.
    """

    serializer_class = AnaliticSerializer

    def get_queryset(self):
        queryset = Like.objects.all()
        date_from = self.request.query_params.get("date_from", None)
        date_to = self.request.query_params.get("date_to", None)
        if date_from is not None and date_to is not None:
            queryset = (
                queryset.filter(created_at__gte=date_from, created_at__lte=date_to)
                .extra(select={"day": "date(created_at)"})
                .values("day")
                .order_by("day")
                .annotate(count=Count("created_at"))
            )
            return queryset
