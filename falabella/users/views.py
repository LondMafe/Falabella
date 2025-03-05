from rest_framework import generics, status
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ChangePasswordSerializer

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

class ChangePasswordView(generics.UpdateAPIView):#Vista para cambiar contraseña
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user #Devuelve usuario que hizo solicitud
    
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        #Verifica contraseña actual incorrecta
        if not user.check_password(serializer.data.get("old_password")):
            return Response({"old_password": ["Contraseña incorrecta."]}, status=status.HTTP_400_BAD_REQUEST)
        
        #Estable nueva contraseña y la guarda
        user.set_password(serializer.data.get("new_password"))
        user.save()
        
        return Response({"detail": "Contraseña actualizada correctamente."}, status=status.HTTP_200_OK)


