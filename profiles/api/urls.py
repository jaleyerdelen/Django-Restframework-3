from django.urls import path, include
from profiles.api.views import ProfileViewSet, ProfileStatusViewSet, ProfilePhotoUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users-profile", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet, basename="status")

urlpatterns = [
    path("", include(router.urls)),
    path("profile-photo/", ProfilePhotoUpdateView.as_view(), name="profile-photo"),
]



#### Bu uzun olduğu için daha kısa versiyonunu yazacağız
# profile_list = ProfileViewSet.as_view({"get": "list"})
# profile_detail = ProfileViewSet.as_view({"get": "retrieve"})

# urlpatterns = [
#     path("users-profile/", profile_list , name="profiles"),
#     path("users-profile/<int:pk>", profile_detail , name="profile-detail"),

# ]
