from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from schedule_collects.models import ScheduleCollect
from schedule_collects.permissions import IsOnlyOwnerSchedule

from users.mixins import SerializerByMethodMixin
from users.models import User
from users.permissions import IsOwnerOrAdmin, IsOwnerSchedule
from users.serializers import (
    UpdateUserSerializer,
    UserScheduleSerializer,
    UserSerializer,
)


def get_object_by_id(model, **kwargs):
    object = get_object_or_404(model, **kwargs)
    return object


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UpdateUserView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):

    permission_classes = [IsOwnerOrAdmin, IsAuthenticated]

    lookup_url_kwarg = "user_id"

    queryset = User.objects.all()

    serializer_map = {
        "PATCH": UpdateUserSerializer,
        "GET": UserSerializer,
    }


class ListUsersView(SerializerByMethodMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = User.objects.all()

    serializer_map = {"GET": UserSerializer}


class UserSchedulesView(generics.ListAPIView):
    permission_classes = [IsOwnerSchedule]

    queryset = User.objects.all()

    serializer_class = UserScheduleSerializer

    lookup_url_kwarg = "id"

    def get_queryset(self):

        user_id = self.kwargs["id"]

        user = ScheduleCollect.objects.filter(user=user_id)

        return user
