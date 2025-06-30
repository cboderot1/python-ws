import reflex as rx


def navbar():
    return rx.flex(
        rx.badge(
            rx.icon(tag="package", size=28),
            rx.heading("Gestión de Tienda", size="6"),
            color_scheme="blue",
            radius="large",
            align="center",
            variant="surface",
            padding="0.65rem",
        ),
        rx.spacer(),
        rx.hstack(
            rx.link("Clientes", href="/clientes"),
            rx.button("Productos", on_click=rx.redirect("/productos")),

            rx.color_mode.button(),
            align="center",
            spacing="3",
        ),
        spacing="2",
        flex_direction=["column", "column", "row"],
        align="center",
        width="100%",
        top="0px",
        padding_top="2em",
    )

