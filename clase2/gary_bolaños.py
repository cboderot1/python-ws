#
# EJERCICIO: Sistema básico de tienda
#

# Parte 1: Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} (stock: {self.stock})"
    
# Parte 2: Clase Tienda
class Tienda:
    def __init__(self):
        self.productos = []

    def registrar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' registrado.")

    def mostrar_productos(self):
        print("\nProductos disponibles:")
        if not self.productos:
            print("La tienda no tiene productos.")
        for i, producto in enumerate(self.productos):
            print(f"{i + 1}. {producto}")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    total = producto.precio * cantidad
                    print(f"Venta realizada: {cantidad} x {producto.nombre} = ${total:.2f}")
                else:
                    print(f"Stock insuficiente. Solo hay {producto.stock} unidades.")
                return
        print(f"Producto '{nombre}' no encontrado.")

#
# # Ejemplo de uso
#

# Crear tienda
mi_tienda = Tienda()

# Registro de productos
p1 = Producto("Pan", 0.25, 60)
p2 = Producto("Huevos", 0.15, 150)
p3 = Producto("Leche", 0.90, 2)
mi_tienda.registrar_producto(p1)
mi_tienda.registrar_producto(p2)
mi_tienda.registrar_producto(p3)

# Mostrar productos
mi_tienda.mostrar_productos()

# Simulador de venta
mi_tienda.vender_producto("Pan", 6)
mi_tienda.vender_producto("Huevos", 5)
mi_tienda.vender_producto("Leche", 3)  # Stock insuficiente
mi_tienda.vender_producto("Queso", 1)  # No existe

# Mostrar productos actualizados
mi_tienda.mostrar_productos()
