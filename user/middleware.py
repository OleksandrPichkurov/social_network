from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from .models import CustomUser


class UpdateLastActivityMiddleware(MiddlewareMixin):
    """
    Middleware for capture the user's last request.
    Update last_activity field in CustomUser model.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(
            request, "user"
        ), "The UpdateLastActivityMiddleware requires authentication middleware to be installed."
        if request.user.is_authenticated:
            CustomUser.objects.filter(email=request.user).update(
                last_activity=timezone.now()
            )
