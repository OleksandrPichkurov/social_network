"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from post.views import AnaliticsLikeListView

urlpatterns = [
    # JWT urls
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # admin
    path("admin/", admin.site.urls),
    # login and logout urls
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # user registration and activity
    path("api/users/", include("user.urls")),
    # actions with post
    path("api/posts/", include("post.urls")),
    # analitics
    path("api/analitics/", AnaliticsLikeListView.as_view(), name="analitics-list"),
]
