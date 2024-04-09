from rest_framework import viewsets
from .models import Categorias, Departamentos, Ciudades, Estado, Marcas, MediosPago, Proveedores, Contactos, TipoIdentificacion, Rol, Usuarios, CarritoCompras, Productos, ProveedoresProductos, Comentarios, Respuestas, DetalleCarrito, Domicilios, ImagenesProducto, Ventas
from .serializer import CategoriasSerializaer, DepartamentosSerializaer, CiudadesSerializaer, EstadoSerializaer, MarcasSerializaer, medios_pagoSerializaer, ProveedoresSerializaer, ContactosSerializaer, TipoIdentificacionSerializaer, RolSerializaer, UsuariosSerializaer, CarritoComprasSerializaer, ProductosSerializaer, ProveedoresProductosSerializaer, ComentariosSerializaer, RespuestasSerializaer, DetalleCarritoSerializaer, DomiciliosSerializaer, ImagenesProductoSerializaer, VentasSerializaer

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializaer

class DepartamentosViewSet(viewsets.ModelViewSet):
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializaer

class CiudadesViewSet(viewsets.ModelViewSet):
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializaer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializaer

class MarcasViewSet(viewsets.ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializaer

class medios_pagoViewSet(viewsets.ModelViewSet):
    queryset = MediosPago.objects.all()
    serializer_class = medios_pagoSerializaer

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializaer

class ContactosViewSet(viewsets.ModelViewSet):
    queryset = Contactos.objects.all()
    serializer_class = ContactosSerializaer


class TipoIdentificacionViewSet(viewsets.ModelViewSet):
    queryset = TipoIdentificacion.objects.all()
    serializer_class = TipoIdentificacionSerializaer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializaer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializaer


class CarritoComprasViewSet(viewsets.ModelViewSet):
    queryset = CarritoCompras.objects.all()
    serializer_class = CarritoComprasSerializaer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializaer

class ProveedoresProductosViewSet(viewsets.ModelViewSet):
    queryset = ProveedoresProductos.objects.all()
    serializer_class = ProveedoresProductosSerializaer


class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializaer

class RespuestasViewSet(viewsets.ModelViewSet):
    queryset = Respuestas.objects.all()
    serializer_class = RespuestasSerializaer


class DetalleCarritoViewSet(viewsets.ModelViewSet):
    queryset = DetalleCarrito.objects.all()
    serializer_class = DetalleCarritoSerializaer

class DomiciliosViewSet(viewsets.ModelViewSet):
    queryset = Domicilios.objects.all()
    serializer_class = DomiciliosSerializaer


class ImagenesProductoViewSet(viewsets.ModelViewSet):
    queryset = ImagenesProducto.objects.all()
    serializer_class = ImagenesProductoSerializaer

class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializaer
