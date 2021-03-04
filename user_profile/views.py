# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from user_profile.serializers import UserSerializer


class RegisterAPIView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
