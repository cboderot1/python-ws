"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""
    pass


def navbar():
    """Barra de navegación simple"""
    return rx.hstack(
        rx.heading("Mi App", size="6", color="blue.600"),
        rx.spacer(),
        rx.hstack(
            rx.link("Inicio", href="/"),
            rx.link("Usuarios", href="/usuarios"),
            rx.link("Categorías", href="/categorias"),
            rx.link("Productos", href="/productos"),
            rx.link("Reportes", href="/reportes"),
            spacing="4"
        ),
        padding="4",
        border_bottom="1px solid #ccc",
        width="100%"
    )


def layout(children):
    """Layout básico"""
    return rx.vstack(
        navbar(),
        rx.container(children, padding="6"),
        spacing="0",
        min_height="100vh"
    )


def index() -> rx.Component:
    """Página principal"""
    return layout(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            rx.heading("¡Bienvenido a Mi Aplicación!", size="9"),
            rx.text("Sistema de gestión simple", size="5"),
            spacing="5",
            justify="center",
            min_height="50vh"
        )
    )


def usuarios() -> rx.Component:
    """Página de usuarios"""
    return layout(
        rx.vstack(
            rx.heading("👥 Usuarios", size="8"),
            rx.text("Aquí irá la gestión de usuarios"),
            spacing="4"
        )
    )


def categorias() -> rx.Component:
    """Página de categorías"""
    return layout(
        rx.vstack(
            rx.heading("🏷️ Categorías", size="8"),
            rx.text("Aquí irá la gestión de categorías"),
            spacing="4"
        )
    )


def productos() -> rx.Component:
    """Página de productos"""
    return layout(
        rx.vstack(
            rx.heading("📦 Productos", size="8"),
            rx.text("Aquí irá la gestión de productos"),
            spacing="4"
        )
    )


def reportes() -> rx.Component:
    """Página de reportes"""
    return layout(
        rx.vstack(
            rx.heading("📊 Reportes", size="8"),
            rx.text("Aquí irán los reportes y estadísticas"),
            spacing="4"
        )
    )


# Configuración de la aplicación
app = rx.App()

app.add_page(index)
app.add_page(usuarios, route="/usuarios")
app.add_page(categorias, route="/categorias")
app.add_page(productos, route="/productos")
app.add_page(reportes, route="/reportes")