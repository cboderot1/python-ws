import reflex as rx
from sqlmodel import String, asc, cast, desc, func, or_, select

class Producto (rx.Model, table=True):
    """el modelo de productos"""
    
    nombre: str
    descripcion: str
    precio: float
    stock: int
    categoria_id: int
    estado: str
    
class ProductoState(rx.State):    
    show_modal: bool = False
    nombre: str = ""
    descripcion: str = ""
    precio: str = ""
    stock: str = ""
    estado: str = ""
    categoria_id: str = ""
    id_edicion: int | None = None
    productos: list[Producto] = []

    def open_add_producto_form(self):
        self.id_edicion = None  # Si usas para editar
        self.nombre = ""
        self.descripcion = ""
        self.precio = ""
        self.stock = ""
        self.estado = ""
        self.categoria_id = ""
        self.show_modal = True
        self.show_modal = True

    def close_modal(self):
        self.show_modal = False

    def set_nombre(self, value: str):
        self.nombre = value

    def set_descripcion(self, value: str):
        self.descripcion = value

    def set_precio(self, value: str):
        self.precio = value

    def set_stock(self, value: str):
        self.stock = value

    def set_estado(self, value: str):
        self.estado = value

    def set_categoria_id(self, value: str):
        self.categoria_id = value

    def submit_producto(self):
        # lógica para guardar producto
        with rx.session() as session:
            nuevo = Producto(
                nombre=self.nombre,
                descripcion=self.descripcion,
                precio=float(self.precio),
                stock=int(self.stock),
                estado=self.estado,
                categoria_id=int(self.categoria_id),
            )
            session.add(nuevo)
            session.commit()
        self.load_productos()
        self.close_modal()
        return rx.toast.success("Producto agregado con éxito.")

    
    def load_productos(self):
        with rx.session() as session:
            self.productos = session.exec(select(Producto)).all()
            
    def editar_producto(self, producto_id: int):
    # Lógica para cargar datos del producto al formulario
        with rx.session() as db:
            producto = db.get(Producto, producto_id)
            if producto:
                self.id_edicion = producto.id
                self.nombre = producto.nombre
                self.descripcion = producto.descripcion
                self.precio = str(producto.precio)
                self.stock = str(producto.stock)
                self.estado = producto.estado
                self.categoria_id = str(producto.categoria_id)
                self.show_modal = True


    def eliminar_producto(self, producto_id: int):
    # Lógica para eliminar el producto
        with rx.session() as session:
            producto = session.get(Producto, producto_id)
            if producto:
                session.delete(producto)
                session.commit()
        self.load_productos()
        return rx.toast.info(f"Producto '{producto.nombre}' eliminado con éxito.")
