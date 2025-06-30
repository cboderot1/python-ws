# views/productos.py
import reflex as rx
from .navbar import navbar  # Asegúrate de que este import sea correcto

def productos_page() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.heading("Lista de Productos"),
        rx.text("Aquí se mostrarán los productos."),
        padding="2em",
        spacing="4",
    )