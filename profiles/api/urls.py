from django.urls import path
from profiles.api import views

urlpatterns = [
    path("users-profile/", views.ProfileList.as_view(), name="profiles"),
]
