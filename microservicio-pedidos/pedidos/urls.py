# pedidos/urls.py

from django.contrib import admin
from django.urls import path, include
from apiPedidos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/usuario/', include('apiPedidos.Usuario.urls')),
    path('', views.home), 
    path('api/direccion/', include('apiPedidos.DireccionEnvio.urls')),
    path('api/pedido/', include('apiPedidos.Pedido.urls')),
   
]
