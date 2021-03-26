from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(
        get_user_model(), related_name="posts", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def like_post(self, user_id):
        like, _ = self.like_set.update_or_create(
            user_id=user_id, defaults={"liked": True}
        )
        return like

    def unlike_post(self, user_id):
        like = self.like_set.filter(user_id=user_id).first()
        if like is not None:
            like.liked = False
            like.save()


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "post")
        # likes that were 'liked again' or recently created will be displayed first
        ordering = ("updated_at",)

    def __str__(self):
        return f"user {self.user.email}, liked {self.post.title}"
