import reflex as rx

# Definimos la clase Producto
class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

# Datos de ejemplo
productos = [
    Producto(1, "Cuaderno", 1.50, 20),
    Producto(2, "Lápiz", 0.30, 100),
    Producto(3, "Borrador", 0.25, 50),
    Producto(4, "Regla", 0.80, 30),
]

# Componente de tabla para mostrar los productos
def tabla_productos():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("ID"),
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Precio"),
                rx.table.column_header_cell("Cantidad")
            )
        ),
        rx.table.body(
            *[
                rx.table.row(
                    rx.table.cell(str(p.id)),
                    rx.table.cell(p.nombre),
                    rx.table.cell(f"${p.precio:.2f}"),
                    rx.table.cell(str(p.cantidad))
                )
                for p in productos
            ]
        )
    )

# Página principal
def index():
    return rx.container(
        rx.heading("Lista de Productos", size="6"),
        tabla_productos()
    )

# Configuración de la app
app = rx.App()
app.add_page(index)
#app.compile()
