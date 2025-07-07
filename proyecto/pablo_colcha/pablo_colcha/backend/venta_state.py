from datetime import datetime, timedelta
from typing import Union,NamedTuple
from pablo_colcha.backend.producto_state import ProductoState

from pablo_colcha.backend.producto_state import Producto
import reflex as rx
from sqlmodel import String, asc, cast, desc, func, or_, select

class Venta(rx.Model, table=True):
    """el modelo de ventas"""
    num_factura: str
    producto_id: int
    cantidad: int
    fecha: datetime = datetime.now()
    
class VentaConProducto(NamedTuple):
    venta: Venta
    nombre_producto: str

    
class VentaState(rx.State):
    num_factura: str = ""
    producto_id: str = ""
    cantidad: str = ""
    ventas: list[Venta] = []

    def set_num_factura(self, value: str):
        self.num_factura = value

    def set_producto_id(self, value: str):
        self.producto_id = value

    def set_cantidad(self, value: str):
        self.cantidad = value
        
    def ventas_con_producto(self) -> list[VentaConProducto]:
        productos = {p.id: p.nombre for p in ProductoState.productos}
        return [
            VentaConProducto(venta=v, nombre_producto=productos.get(v.producto_id, "Desconocido"))
            for v in self.ventas
        ]
    def registrar_venta(self):
        try:
            cantidad_int = int(self.cantidad)
            if cantidad_int <= 0:
                return rx.toast.warning("Cantidad inválida.")

            with rx.session() as session:
                producto = session.get(Producto, int(self.producto_id))
                if not producto:
                    return rx.toast.error("Producto no encontrado.")

                if producto.stock < cantidad_int:
                    return rx.toast.warning("Stock insuficiente para realizar la venta.")

                # Crear la venta
                venta = Venta(
                    num_factura=self.num_factura,
                    producto_id=producto.id,
                    cantidad=cantidad_int
                )
                session.add(venta)

                # Restar del stock
                producto.stock -= cantidad_int
                session.add(producto)

                session.commit()

            self.load_ventas()
            return rx.toast.success("Venta registrada y stock actualizado.")
        except Exception as e:
            return rx.toast.error(f"Error al registrar venta: {e}")

    def load_ventas(self):
        with rx.session() as session:
            self.ventas = session.exec(select(Venta)).all()
    