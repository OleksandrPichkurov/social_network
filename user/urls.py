from rest_framework import routers

from .views import UserActivityView, UserRegisterView

router = routers.SimpleRouter()

router.register("signup", UserRegisterView, basename="register")
router.register("activity", UserActivityView, basename="activity")

urlpatterns = router.urls
