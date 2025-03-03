from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all() #Vista de usuarios y registros
    serializer_class = UserSerializer

    def get_permissions(self):#Permite registro de usuario pero GET requiere permisos
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):#Vista para actualizar o eliminar usuario esp.
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


