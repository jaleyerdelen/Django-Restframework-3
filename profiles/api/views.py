from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile, ProfileStatus
from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer, ProfilePhotoSerializer
#from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from profiles.api.permissions import OwnProfileOrReadOnly, StatusOwnProfileOrReadOnly
from rest_framework.filters import SearchFilter

class ProfileViewSet(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                GenericViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, OwnProfileOrReadOnly]
    filter_backends = [SearchFilter]
    search_filters = ["city"]

class ProfileStatusViewSet(ModelViewSet):
    
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, StatusOwnProfileOrReadOnly]

    #http://127.0.0.1:8000/api/status/?username=jale
    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
            return queryset 

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)

class ProfilePhotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilePhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_instance = self.request.user.profile
        return profile_instance
