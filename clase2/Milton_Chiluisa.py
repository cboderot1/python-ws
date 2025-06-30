# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"{self.nombre} | Precio: ${self.precio} | Stock: {self.stock}")

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"El stock de {self.nombre} ahora es: {self.stock}")

    def vender(self, cantidad):
        if cantidad <= self.stock:
            total = cantidad * self.precio
            self.stock -= cantidad
            print(f"Venta exitosa: {cantidad} unidades de {self.nombre}. Total a pagar: ${total}")
            return total
        else:
            print(f"Error: No hay suficiente stock de {self.nombre}. Stock disponible: {self.stock}")
            return 0


# Clase Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado a la tienda.")

    def listar_productos(self):
        print(f"\nTienda Online: {self.nombre}\n")
        print("Productos disponibles:\n")
        for producto in self.productos:
            producto.mostrar_info()
        print("\n")

    def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                producto.vender(cantidad)
                return
        print(f"Producto '{nombre_producto}' no encontrado en la tienda.")


# ----------------------
# Programa principal

# Crear la tienda
tienda = Tienda("EVOLUM Store")

# Crear productos
producto1 = Producto("Ligas", 50.0, 200)
producto2 = Producto("Perfumes", 60.0, 60)

# Agregar productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

# Mostrar listado de productos
tienda.listar_productos()

# Simular ventas
tienda.vender_producto("Ligas", 5)
tienda.vender_producto("Perfumes", 2)

# Mostrar productos después de ventas
tienda.listar_productos()
