# dominic_munoz.py

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}")

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            total = self.precio * cantidad
            return f"Total a pagar: ${total:.2f}"
        else:
            return f"Error: Stock insuficiente para '{self.nombre}'. Stock disponible: {self.stock}"


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        print(f"\nTienda: {self.nombre}\n")
        print("Productos disponibles:\n")
        for producto in self.productos:
            producto.mostrar_info()

    def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                print(f"\nVendiendo {cantidad} {producto.nombre}(s)...")
                print(producto.vender(cantidad))
                return
        print(f"\nProducto '{nombre_producto}' no encontrado.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    pan = Producto("Pan", 0.50, 20)
    jugo = Producto("Jugo", 1.25, 10)

    # Crear tienda
    tienda = Tienda("Super Market")

    # Agregar productos a la tienda
    tienda.agregar_producto(pan)
    tienda.agregar_producto(jugo)

    # Listar productos
    tienda.listar_productos()

    # Vender productos
    tienda.vender_producto("Jugo", 3)

    # Mostrar stock actualizado
    print("\nStock actualizado:\n")
    jugo.mostrar_info()
