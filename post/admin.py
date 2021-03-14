from django.contrib import admin

from .models import Like, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ("created_at",)
    list_display = ["id", "title", "content", "author", "created_at"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    ordering = ("updated_at",)
