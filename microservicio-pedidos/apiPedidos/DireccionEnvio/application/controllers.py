from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apiPedidos.DireccionEnvio.domain.services import DireccionEnvioService
from apiPedidos.DireccionEnvio.serializers import DireccionEnvioSerializer, EditDIreccionSerializer,DirecciondtoSerializer, UpdateDireccionSerializer
from apiPedidos.DireccionEnvio.dtos.direcciondto import Direcciondto
from apiPedidos.DireccionEnvio.dtos.updatedireccion import UpdateDirecciondto
from apiPedidos.DireccionEnvio.exceptions.DireccionEnvio_exceptions import DireccionNotFound, InvalidDireccionException, UsuarioNotFoundDireccion

class DireccionEnvioGuardar(APIView):
    def post(self, request):
        serializer = DireccionEnvioSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            try:
                print("Datos validos", serializer.data)
                direccion = DireccionEnvioService.createDireccionEnvio(
                    direccion_data=serializer.data
                )
                return Response({
                    'message': 'Direccion creada correctamente',
                    "Direccion": serializer.data
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                print("error en el try" )
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("error en serializer")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({
            'message': 'Para registrar una dirección, usa el método POST con los siguientes campos:',
            'fields': DireccionEnvioSerializer().data
        }, status=status.HTTP_200_OK)
   
class DireccionEnvioDetalles(APIView):
    def get(self, request, *args, **kwargs):
        direccionId= kwargs.get('direccionId')
        try:
            print("DireccionId", direccionId)
            direccion = DireccionEnvioService.get_direccionById(direccionId)
            print("Direccion encontrada", direccion)
            serializer = DirecciondtoSerializer(direccion)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class DireccioEnvioByUser(APIView):
    def get(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')
        if not idUsuario:
            return Response({"error": "idUsuario es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            direcciones = DireccionEnvioService.get_direccionesByUserId(idUsuario)
            print(direcciones)
            serializer = DirecciondtoSerializer(direcciones, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("error en el try")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        
class DireccionEnvioDelete(APIView):
    def delete(self, request, *args, **kwargs):
        direccionId = kwargs.get('direccionId')
        try:
            DireccionEnvioService.deleteDireccion(direccionId)
            return Response({
                'message': 'Direccion eliminada correctamente',
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DireccionEnvioEditar(APIView):
    def put(self, request, *args, **kwargs): 
        direccionId = kwargs.get('direccionId')
        if(not direccionId):
            return Response({"error": "direccionId es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        usuarioId = kwargs.get('usuarioId')
        if(not usuarioId):
            return Response({"error": "usuarioId es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UpdateDireccionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                direccion_dto = UpdateDirecciondto(
                    direccion=serializer.validated_data['direccion'],
                    distrito=serializer.validated_data['distrito'],
                    provincia=serializer.validated_data['provincia'],
                    departamento=serializer.validated_data['departamento'],
                    pais=serializer.validated_data['pais'],
                    codigoPostal=serializer.validated_data['codigoPostal'],
                    instrucciones=serializer.validated_data['instrucciones'],
                    latitud=serializer.validated_data['latitud'],
                    longitud=serializer.validated_data['longitud']
                )
                DireccionEnvioService.EditarDireccion(direccionId, usuarioId, direccion_dto)
                return Response(
                    {
                        'message': 'Direccion actualizada correctamente',
                    }, status=status.HTTP_200_OK
                )
            except DireccionNotFound as e:
                return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except UsuarioNotFoundDireccion as e:
                return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)