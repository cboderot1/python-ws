# views/productos.py
import reflex as rx
from .navbar import navbar
from pablo_colcha.backend.backend import State as ProductoState # Asegúrate de que este import sea correcto

def productos_page() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.heading("Lista de Productos", size="5", padding_bottom="1em"),
        #rx.button("Cargar productos", on_click=ProductoState.load_productos),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("ID"),
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell("Descripción"),
                    rx.table.column_header_cell("Precio"),
                    rx.table.column_header_cell("Stock"),
                    rx.table.column_header_cell("Estado"),
                )
            ),
            rx.table.body(
                rx.foreach(
                    ProductoState.productos,
                    lambda p: rx.table.row(
                        rx.table.cell(p.id),
                        rx.table.cell(p.nombre),
                        rx.table.cell(p.descripcion),
                        rx.table.cell(f"${p.precio:.2f}"),
                        rx.table.cell(p.stock),
                        rx.table.cell(p.estado),
                    )
                )
            ),
            width="100%",
            variant="surface"
        ),
        padding="2em"
    )

