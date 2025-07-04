import reflex as rx

from .components.stats_cards import stats_cards_group
from .views.navbar import navbar
from .views.table import main_table
from pablo_colcha.views.productos_page import productos_page
from .views.ventas_page import pagina_ventas


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        stats_cards_group(),
        rx.box(
            main_table(),
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="grass"
    ),
)

app.add_page(
    index,
    title="Customer Data App",
    description="A simple app to manage customer data.",
)

app.add_page(
    productos_page,
    route="/productos",  # Ruta para que funcione en /productos
    title="Productos",
    description="Página de productos",
)

app.add_page(
    pagina_ventas, route="/ventas", title="Gestión de Ventas")

