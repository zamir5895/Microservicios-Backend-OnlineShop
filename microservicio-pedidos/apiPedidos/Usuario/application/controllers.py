from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apiPedidos.Usuario.domain.services import UsuarioService
from apiPedidos.Usuario.serializers import UsuarioSerializer, UsuarioLoginSerializer, EmailSerializer, TelefonoSerializer
from apiPedidos.Usuario.exceptions.Usuario_exceptions import UsuarioException
from apiPedidos.Usuario.domain.models import Usuario  
from apiPedidos.Usuario.dtos.Usuario_dto import UsuarioDto

class UsuarioRegisterView(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            try:
                usuario = UsuarioService.createUsuario(
                    nombre=serializer.validated_data['nombre'],
                    apellido=serializer.validated_data['apellido'],
                    email=serializer.validated_data['email'],
                    telefono=serializer.validated_data['telefono']
                )
                return Response({
                    'message': 'Usuario creado correctamente',
                    "Usuario": serializer.data
                }, status=status.HTTP_201_CREATED)
            except UsuarioException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        return Response({
            'message': 'Para registrar un usuario, usa el método POST con los siguientes campos:',
            'fields': UsuarioSerializer().data
        }, status=status.HTTP_200_OK)
        
class UsuarioLoginView(APIView):
    def post(self, request):
        serializer = UsuarioLoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                usuario = UsuarioService.login_usuario(
                    email = serializer.validated_data['email'],
                )
                serializerInfo = UsuarioSerializer(usuario)
                return Response({
                    'message': 'Usuario logueado correctamente',
                    "Usuario": serializerInfo.data
                    
                }, status=status.HTTP_200_OK)
            except UsuarioException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        return Response({
            'message': 'Para loguear un usuario, usa el método POST con los siguientes campos:',
            'fields': UsuarioLoginSerializer().data
        }, status=status.HTTP_200_OK)
    
class UsuarioDetalles(APIView):
    def get(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')  # Extraer idUsuario de kwargs
        try:
            usuario = UsuarioService.get_user_by_id(idUsuario)
            serializer = UsuarioSerializer(usuario)
            return Response({
                'message': 'Usuario encontrado',
                "Usuario": serializer.data
            }, status=status.HTTP_200_OK)
        except UsuarioException as e:
            return Response({"error usuario no encontrado": str(e)}, status=status.HTTP_404_NOT_FOUND)

class UsuarioDetallesEmail(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({
                'error': 'El email es requerido'
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            usuario = UsuarioService.get_user_email(email)
            serializer = UsuarioSerializer(usuario)
            return Response({
                'message': 'Usuario encontrado',
                "Usuario": serializer.data
            }, status=status.HTTP_200_OK)
        except UsuarioException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

        
class ObtenerId(APIView):
    def get(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')  # Extraer idUsuario de kwargs
        try:
            usuario = UsuarioService.get_user_id(idUsuario)
            return Response({
                'message': 'Usuario encontrado',
                "Usuarioid": usuario.idUsuario,
            }, status=status.HTTP_200_OK)
        except UsuarioException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

        
class UsuarioDelete(APIView):
    def delete(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')  # Extraer idUsuario de kwargs
        try:
            UsuarioService.deleteUsuario(idUsuario)
            return Response({
                'message': 'Usuario eliminado'
            }, status=status.HTTP_200_OK)
        except UsuarioException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)


class UsuarioUpdateEmail(APIView):
    def put(self, request,*args, **kwargs):
        idUsuario = kwargs.get('idUsuario')  # Extraer idUsuario de kwargs
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                UsuarioService.update_email(
                    idUsuario=idUsuario,
                    email=serializer.validated_data['email']
                )
                return Response({
                    'message': 'Email actualizado'
                }, status=status.HTTP_200_OK)
            except UsuarioException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    
class updateTelefono(APIView):
    def put(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')  # Extraer idUsuario de kwargs
        serializer = TelefonoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                UsuarioService.update_telefono(
                    idUsuario=idUsuario,
                    telefono=serializer.validated_data['telefono']
                )
                return Response({
                    'message': 'Telefono actualizado'
                }, status=status.HTTP_200_OK)
            except UsuarioException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateUsuario(APIView):
    def put(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')
        try:
            usuario = UsuarioService.get_user_by_id(idUsuario)
        except UsuarioException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            try:
                usuario_dto = UsuarioDto(
                    idUsuario=idUsuario,
                    nombre=serializer.validated_data['nombre'],
                    apellido=serializer.validated_data['apellido'],
                    email=serializer.validated_data['email'],
                    telefono=serializer.validated_data['telefono']
                )
                UsuarioService.update_all_usuario(usuario_dto)
                return Response({
                    'message': 'Usuario actualizado'
                }, status=status.HTTP_200_OK)
            except UsuarioException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    