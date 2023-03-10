from .models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

from rest_framework.response import Response
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny # ¿temporal?
    ]
    serializer_class = UserSerializer
    lookup_field = "email"
    lookup_value_regex = "[^/]+"