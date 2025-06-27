# /////////////////////////// Parte 1: Clase Producto ///////////////////////////
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
        if self.stock >= cantidad:
            total = self.precio * cantidad
            self.stock -= cantidad
            return total
        else:
            return f"No hay suficiente stock de {self.nombre} (Stock disponible: {self.stock})"


# ///////////////////////////Parte 2: Clase Tienda ///////////////////////////
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = [] #Creo una lista vacia donde se van a almacenar los productos

    def agregar_producto(self, producto):
        self.productos.append(producto) #añade un objeto Producto a la lista productos

    def listar_productos(self):
        print(f"\nTienda: {self.nombre}")
        print("\nProductos disponibles:\n")
        for producto in self.productos:
            producto.mostrar_info() # lista todos los productos

    def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos: #busca un producto por nombre para la venta
            if producto.nombre.lower() == nombre_producto.lower(): # lower compara sin importar mayusculas
                resultado = producto.vender(cantidad) # llamo al metodo vender
                if isinstance(resultado, float): # si la venta tubo exito
                    print(f"\nVendiendo {cantidad} {producto.nombre.lower()}(s)... Total a pagar: ${resultado:.2f}")
                else:
                    print("\n" + resultado)
                return
        print(f"\nProducto '{nombre_producto}' no encontrado en la tienda.")

# /////////////////////////// PRPRODUCTOS  ///////////////////////////
if __name__ == "__main__":
    # Crear productos
    pan = Producto("Pan", 0.50, 20)
    jugo = Producto("Jugo", 1.25, 10)
    leche = Producto("Leche", 2.75, 9)

    # Crear tienda y agregar productos
    tienda = Tienda("Tuti")
    tienda.agregar_producto(pan)
    tienda.agregar_producto(jugo)
    tienda.agregar_producto(leche)

    # Listar productos
    tienda.listar_productos()

    # Vender producto (3 unidades)
    tienda.vender_producto("Jugo", 3)
    tienda.vender_producto("leche", 2)

    # Mostrar stock actualizado despues de la venta
    print("\nStock actualizado:\n")
    jugo.mostrar_info()