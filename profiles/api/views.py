from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile
from profiles.api.serializers import ProfileSerializer
#from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from profiles.api.permissions import OwnProfileOrReadOnly

class ProfileViewSet(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                GenericViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, OwnProfileOrReadOnly]