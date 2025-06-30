import reflex as rx
from pablo_colcha.backend.producto_state import ProductoState

from pablo_colcha.backend.producto_state import Producto

from pablo_colcha.backend.venta_state import VentaState
from pablo_colcha.backend.venta_state import Venta,VentaConProducto


from .navbar import navbar

def pagina_ventas():
    return rx.container(
        rx.vstack(
            navbar(),
            formulario_venta(),
            tabla_ventas(),
            spacing="8",
        ),
        on_mount=lambda: [ProductoState.load_productos(), VentaState.load_ventas()],
    )

def formulario_venta():
    return rx.vstack(
        rx.heading("Registrar Venta", size="4"),
        rx.input(
            placeholder="Número de Factura",
            value=VentaState.num_factura,
            on_change=VentaState.set_num_factura,
        ),
        rx.select.root(
            rx.select.trigger(placeholder="Selecciona un producto"),
            rx.select.content(
                rx.foreach(
                    ProductoState.productos,
                    lambda p: rx.select.item(
                        label=p.nombre,
                        value=str(p.id),
                    ),
                )
            ),
            value=VentaState.producto_id,
            on_change=VentaState.set_producto_id,
        ),
        rx.input(
            placeholder="Cantidad",
            value=VentaState.cantidad,
            on_change=VentaState.set_cantidad,
            type_="number",
        ),
        rx.button("Registrar Venta", on_click=VentaState.registrar_venta, color="green"),
        spacing="4",
        padding="4",
        border="2px solid #ccc",
        border_radius="4",
        width="100%",
    )

def fila(venta: Venta):
    def render_row():
        productos = {p.id: p.nombre for p in ProductoState.productos}
        nombre_producto = productos.get(venta.producto_id, "Desconocido")

        return rx.tr(
            rx.td(venta.num_factura),
            rx.td(nombre_producto),
            rx.td(str(venta.cantidad)),
            rx.td(venta.fecha.strftime("%Y-%m-%d %H:%M")),
        )
    
    return rx.cond(VentaState.ventas is not None, render_row, rx.tr(rx.td("Cargando...")))


def tabla_ventas():
    def fila(v):
        producto = next((p for p in ProductoState.productos if p.id == v.producto_id), None)
        nombre_producto = producto.nombre if producto else "Desconocido"
        return rx.hstack(
            rx.text(f"Factura: {v.num_factura}"),
            rx.text(f"Producto: {nombre_producto}"),
            rx.text(f"Cantidad: {v.cantidad}"),
            rx.text(f"Fecha: {v.fecha.strftime('%Y-%m-%d %H:%M')}"),
            spacing="4",
            padding="2",
            border="1px solid #ccc",
            border_radius="8px",
            width="100%",
        )

    """return rx.vstack(
            rx.heading("Listado de Ventas", size="4"),
            rx.foreach(VentaState.ventas_con_producto, fila),
        
            padding="4",
            border="2px solid #ccc",
            border_radius="4",
            width="100%",
        )"""


