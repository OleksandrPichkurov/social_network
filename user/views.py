from rest_framework import mixins, viewsets

from .models import CustomUser
from .permissions import ReadOnly
from .serializers import RegisterCustomUserSerializer, UserActivitySerializer


class UserRegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    User register view
    This view will create user and return an user
    """

    queryset = CustomUser.objects.all()
    serializer_class = RegisterCustomUserSerializer


class UserActivityView(viewsets.ModelViewSet):
    """
    User activiti view
    This view will return an users last request and login
    """

    permission_classes = [ReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = UserActivitySerializer
