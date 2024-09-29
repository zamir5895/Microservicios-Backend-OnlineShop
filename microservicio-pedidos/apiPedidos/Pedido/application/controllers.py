from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apiPedidos.Pedido.domain.services import PedidoService
from apiPedidos.Pedido.serializers import PedidoSerializer, EditPedidoSerializer, PedidoDtoSerializer
from apiPedidos.Pedido.dtos.Pedido_dto import Pedidodto
from apiPedidos.Pedido.exceptions.Pedido_exceptions import PedidoNotFound, InvalidPedidoException, UsuarioNotFoundPedido, DireccionNotFoundPedido
from apiPedidos.Pedido.dtos.updatePedidodto import UpdatePedidodto

class PedidoGuardar(APIView):
    def post(self, request):
        serializer = PedidoSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            try:
                print("Datos validos", serializer.data)
                pedido = PedidoService.createPedido(
                    pedido_data=serializer.data
                )
                return Response({
                    'message': 'Pedido creado correctamente',
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                print("error en el try" )
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("error en serializer")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        return Response({
            'message': 'Para registrar un pedido, usa el método POST con los siguientes campos:',
            'fields': PedidoSerializer().data
        }, status=status.HTTP_200_OK)
    
class DetallesPedidoId(APIView):
    def get(self, request, *args, **kwargs):
        pedidoId = kwargs.get('pedidoId')
        if not pedidoId:
            return Response({"error": "Falta el ID del pedido"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            pedido = PedidoService.getPedidoById(pedidoId)
            serializer = PedidoDtoSerializer(pedido)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class PedidoByUserId(APIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        if not userId:
            return Response({"error": "Falta el ID del usuario"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            pedidos = PedidoService.getPedidosByUserId(userId)
            serializer = PedidoDtoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class PedidoByUserIdAndPedidoId(APIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        pedidoId = kwargs.get('pedidoId')
        if not userId or not pedidoId:
            return Response({"error": "Falta el ID del usuario o del pedido"}, status=status.HTTP_400_BAD_REQUEST)
        try:

            pedido = PedidoService.getPedidoByUserIdAndPedidoId(userId, pedidoId)
            serializer = PedidoDtoSerializer(pedido)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except UsuarioNotFoundPedido as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except DireccionNotFoundPedido as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        
class PedidoByUserIdAndEstado(APIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        if not userId:
            return Response({"error": "Falta el ID del usuario"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            estado = request.query_params.get('estado')
            pedidos = PedidoService.getPeidosByUserIdAndEstado(userId, estado)
            serializer = PedidoDtoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PedidoByUserIdAndFechaPedido(APIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        fechaPedidodesde = request.query_params.get('fechaPedidodesde')
        fechaPedidoHasta = request.query_params.get('fechaPedidoHasta')
        if not userId or not fechaPedidodesde or not fechaPedidoHasta:
            return Response({"error": "Falta el ID del usuario o de las fechas"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            pedidos = PedidoService.getPedidoByUserIdAndFechaPedido(userId, fechaPedidodesde, fechaPedidoHasta)
            serializer = PedidoDtoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class PedidosByEstado(APIView):
    def get(self, request, *args, **kwargs):
        estado = request.query_params.get('estado')
        if not estado:
            return Response({"error": "Falta el estado del pedido"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            pedidos = PedidoService.getPedidosByEstado(estado)
            serializer = PedidoDtoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PedidosByRangeFechaPedido(APIView):
    def get(self, request, *args, **kwargs):
        fechaPedidodesde = request.query_params.get('fechaPedidodesde')
        fechaPedidoHasta = request.query_params.get('fechaPedidoHasta')
        if not fechaPedidodesde or not fechaPedidoHasta:
            return Response({"error": "Falta el rango de fechas"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            pedidos = PedidoService.getPedidosByRangeFechaPedido(fechaPedidodesde, fechaPedidoHasta)
            serializer = PedidoDtoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class PedidoEditar(APIView):
    def put(self, request, *args, **kwargs):
        pedidoId = kwargs.get('pedidoId')
        if(not pedidoId):
            return Response({"error": "pedidoId es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = EditPedidoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                pedido_dto = UpdatePedidodto(
                    fecha_entrega=serializer.validated_data['fechaEntrega'],   
                    estado_pedido=serializer.validated_data['estado'],
                    total_pedido=serializer.validated_data['total'],
                    observaciones=serializer.validated_data['observaciones']
                )
                PedidoService.EditarPedido(pedidoId, pedido_dto)
                return Response(
                    {
                        'message': 'Pedido actualizado correctamente',
                    }, status=status.HTTP_200_OK
                )
            except PedidoNotFound as e:
                return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
            except InvalidPedidoException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PedidoDelete(APIView):
    def delete(self, request, *args, **kwargs):
        pedidoId = kwargs.get('pedidoId')
        try:
            PedidoService.deletePedido(pedidoId)
            return Response({
                'message': 'Pedido eliminado correctamente',
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)