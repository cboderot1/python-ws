# Clase Producto (con métodos para actualizar stock y vender)

class Producto:
    # Constructor de producto
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    # Muestra la información del producto
    def mostrar_info(self):
        print(f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}")
    # Actualiza el stock
    def actualizar_stock(self, cantidad):
        self.stock += cantidad
    # Vende el producto
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return self.precio * cantidad
        else:
            return f"No hay suficiente stock de {self.nombre} (Stock: {self.stock})"

# Clase Tienda (con métodos para agregar, listar y vender productos)
class Tienda:
    # Constructor de tienda
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    #   Agrega un producto
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado con éxito.")
    #   Muestra los productos disponibles
    def listar_productos(self):
        print(f"\nProductos disponibles en {self.nombre}:")
        for i, producto in enumerate(self.productos, start=1):
            print(f"{i}. ", end="")
            producto.mostrar_info()
            
    #   Vende el producto seleccionado por el indice
    def vender_producto(self, indice, cantidad):
        if 0 <= indice < len(self.productos):
            producto = self.productos[indice]
            resultado = producto.vender(cantidad)
            if isinstance(resultado, float):
                print(f"\nVendiendo {cantidad} {producto.nombre}(s)...")
                print(f"Total a pagar: ${resultado:.2f}")
            else:
                print(resultado)
        else:
            print("Opción inválida.")

# Menú principal
def menu_tienda():
    tienda = Tienda("Super Market")
    # Bucle para el menú principal
    while True:
        print("\n--- Menú de la Tienda ---")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Vender producto")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        # Opciones del menú apartir de la selección
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                stock = int(input("Cantidad en stock: "))
                nuevo = Producto(nombre, precio, stock)
                tienda.agregar_producto(nuevo)
            except ValueError:
                print("Error: Ingresa un precio y stock válidos.")
                #listar_productos
        elif opcion == "2":
            tienda.listar_productos()
            #venta de productos
        elif opcion == "3":
            if not tienda.productos:
                print("No hay productos disponibles.")
                continue
            tienda.listar_productos()
            try:
                seleccion = int(input("Seleccione el número del producto a vender: ")) - 1
                cantidad = int(input("Cantidad a vender: "))
                tienda.vender_producto(seleccion, cantidad)
            except ValueError:
                print("Entrada inválida.")
                #salir del programa
        elif opcion == "4":
            print("¡Gracias por usar la tienda!")
            break
        else:
            print("Opción no válida.")

# Ejecutar el menú
if __name__ == "__main__":
    menu_tienda()


