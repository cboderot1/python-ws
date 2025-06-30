
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def mostrar_info(self):
        print(f"{self.nombre} | Precio: ${self.precio:.2f}, | Stock: {self.stock}")
    
    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        
    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            total_a_pagar = self.precio * cantidad
            return total_a_pagar
        else:
            return f"Error: No hay suficiente stock de {self.nombre}. Stock actual: {self.stock}"
        
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f" Se ha agregado el producto: {producto.nombre} a la tienda")
        
    def listar_productos(self):
        print(f"\nTienda: {self.nombre}")
        print("Productos disponibles:")
        for producto in self.productos:
            producto.mostrar_info()
            
    def vender_producto(self, nombre_producto, cantidad):
        print(f"\nVendiendo {cantidad} {nombre_producto}...")
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                resultado_venta = producto.vender(cantidad)
                if isinstance(resultado_venta, (int, float)):
                    print(f" Venta exitosa. Total a pagar: ${resultado_venta:.2f}")
                    print("Stock actualizado:")
                    producto.mostrar_info()
                else:
                    print(resultado_venta)
                return
        print(f" El producto '{nombre_producto}' no se encuentra en la tienda.")

if __name__ == "__main__":
    pan = Producto("Pan", 0.50, 20)
    jugo = Producto("Jugo", 1.25, 10)
    leche = Producto("Leche", 2.00, 5)

    super_market = Tienda("Super Market")

    super_market.agregar_producto(pan)
    super_market.agregar_producto(jugo)
    super_market.agregar_producto(leche)

    super_market.listar_productos()

    super_market.vender_producto("Jugo", 3)

    super_market.vender_producto("Leche", 6)

    super_market.vender_producto("Gaseosa", 1)

    super_market.listar_productos()