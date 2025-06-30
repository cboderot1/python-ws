import reflex as rx
from pablo_colcha.backend.producto_state import ProductoState

from pablo_colcha.backend.producto_state import Producto

from .navbar import navbar

def productos_page() -> rx.Component:
    
    return rx.vstack(
        navbar(),
        
        rx.heading("Lista de Productos", size="5", padding_bottom="2"),
        
        
        rx.button(
            "Agregar producto",
            on_click=ProductoState.open_add_producto_form,
            color_scheme="green",
            margin_bottom="4",
            on_mount=ProductoState.load_productos,
        ),
        

        # Diálogo (sin usar .overlay, .header, etc.)
        rx.dialog.root(
            rx.dialog.trigger(rx.button("Abrir modal (debug)", display="none")),  # Se puede ocultar
            rx.dialog.content(
                rx.vstack(
                    rx.dialog.title("Agregar Producto"),
                    rx.vstack(
                        rx.input(
                            placeholder="Nombre",
                            value=ProductoState.nombre,
                            on_change=ProductoState.set_nombre,
                        ),
                        rx.text_area(
                            placeholder="Descripción",
                            value=ProductoState.descripcion,
                            on_change=ProductoState.set_descripcion,
                        ),
                        rx.input(
                            placeholder="Precio",
                            type="number",
                            value=ProductoState.precio,
                            on_change=ProductoState.set_precio,
                        ),
                        rx.input(
                            placeholder="Stock",
                            type="number",
                            value=ProductoState.stock,
                            on_change=ProductoState.set_stock,
                        ),
                        rx.radio_group.root(
                            rx.text("Status", size="3",align="center",spacing="2"),
                            rx.radio_group.item("Activo", value="Activo"),
                            rx.radio_group.item("Inactivo", value="Inactivo"),
                                value=ProductoState.estado,
                                on_change=ProductoState.set_estado,
                                flex_direction="row",  # O "column" si prefieres vertical
                                spacing="4",
                        ),


                        rx.input(
                            placeholder="Categoría ID",
                            type="number",
                            value=ProductoState.categoria_id,
                            on_change=ProductoState.set_categoria_id,
                        ),
                        rx.hstack(
                            rx.button(
                                "Cancelar",
                                on_click=ProductoState.close_modal,
                                color_scheme="red",
                            ),
                            rx.button(
                                "Guardar",
                                on_click=ProductoState.submit_producto,
                                color_scheme="blue",
                            ),
                        ),
                        spacing="4"
                    ),
                ),
                padding="2",
            ),
            open=ProductoState.show_modal,
        ),

        # Tabla de productos
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("ID"),
                    rx.table.column_header_cell("Nombre"),
                    #rx.icon(tag="users", size=15),
                    rx.table.column_header_cell("Descripción"),
                    rx.table.column_header_cell("Precio"),
                    rx.table.column_header_cell("Stock"),
                    rx.table.column_header_cell("Estado"),
                    rx.table.column_header_cell("Acciones"),
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
                        rx.table.cell(  # Acciones
                            rx.hstack(
                                rx.button(
                                    "Editar",
                                    size="2",
                                    color_scheme="blue",
                                    on_click=lambda: ProductoState.editar_producto(p.id),
                                ),
                                rx.button(
                                    "Eliminar",
                                    size="2",
                                    color_scheme="red",
                                    on_click=lambda: ProductoState.eliminar_producto(p.id),
                                ),
                                spacing="2",
                            )
                        ),
                    )
                )
            ),
            width="100%",
            variant="surface"
        ),

        padding="4",
    )
