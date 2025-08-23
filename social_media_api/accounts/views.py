# accounts/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer

class UserListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
