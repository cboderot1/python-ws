class Tienda:
    """Clase base que representa una tienda"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    
    def agregar_producto(self, producto):
        """Añade un producto a la tienda"""
        self.productos.append(producto)
    
    def listar_productos(self):
        """Imprime todos los productos disponibles"""
        print(f"\nTienda: {self.nombre}")
        print("\nProductos disponibles:\n")
        for producto in self.productos:
            producto.mostrar_info()
    
    def buscar_producto(self, nombre_producto):
        """Busca un producto por nombre"""
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                return producto
        return None


class Producto(Tienda):
    """Clase Producto que hereda de Tienda"""
    
    def __init__(self, nombre, precio, stock, nombre_tienda="Mi Tienda"):
        # Llamar al constructor de la clase padre (Tienda)
        super().__init__(nombre_tienda)
        
        # Atributos específicos del producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        """Muestra la información del producto"""
        print(f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}")
    
    def actualizar_stock(self, cantidad):
        """Actualiza el stock del producto"""
        self.stock += cantidad
        if self.stock < 0:
            self.stock = 0
    
    def vender(self, cantidad):
        """Vende una cantidad del producto"""
        if cantidad <= self.stock:
            self.stock -= cantidad
            return cantidad * self.precio
        else:
            return f"❌ Stock insuficiente. Solo hay {self.stock} unidades disponibles."
    
    def vender_producto(self, nombre_producto, cantidad):
        """
        Método heredado y sobrescrito para vender productos
        En este caso, vende el producto actual si coincide el nombre
        """
        if self.nombre.lower() == nombre_producto.lower():
            print(f"\nVendiendo {cantidad} {nombre_producto}...")
            resultado = self.vender(cantidad)
            
            if isinstance(resultado, float):
                print(f"Total a pagar: ${resultado:.2f}")
                print(f"\nStock actualizado:")
                print(f"{self.nombre} | Stock: {self.stock}")
            else:
                print(resultado)
        else:
            print(f"❌ Este producto no es '{nombre_producto}'")


# Ejemplo de uso
def main():
    # Crear productos en la tienda
    pan = Producto("Pan", 0.50, 20, "Super Market")
    jugo = Producto("Jugo", 1.25, 10, "Super Market")
    
    # Crear una tienda principal
    tienda_principal = Tienda("Super Market")
    
    # Agregar productos a la tienda
    tienda_principal.agregar_producto(pan)
    tienda_principal.agregar_producto(jugo)
    
    # Mostrar productos  en la tienda
    tienda_principal.listar_productos()
    
    print("\n" + "="*40)
    print("Proceso")
    print("="*40)
    
    print(f"\nEl producto 'Pan' pertenece a la tienda: {pan.nombre}")
    print(f"Productos en la tienda del Pan: {len(pan.productos)}")
    
    # Agregar otros productos a la tienda del producto 'pan'
    leche = Producto("Leche", 2.00, 15, "Super Market")
    pan.agregar_producto(leche)
    
    print(f"Después de agregar leche: {len(pan.productos)} productos")
    
    print("\n" + "="*40)
    print("VENTAS")
    print("="*40)
    
    # Venta usando producto
    jugo.vender_producto("Jugo", 3)
    
    print("\n" + "-"*30)
    
    # Venta usando el método de búsqueda de la tienda
    producto_encontrado = tienda_principal.buscar_producto("Pan")
    if producto_encontrado:
        print(f"\nVendiendo 5 panes...")
        resultado = producto_encontrado.vender(5)
        if isinstance(resultado, float):
            print(f"Total a pagar: ${resultado:.2f}")
            print(f"Stock actualizado:")
            producto_encontrado.mostrar_info()

if __name__ == "__main__":
    main()