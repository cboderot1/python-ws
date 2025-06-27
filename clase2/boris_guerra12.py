# clase 2 Ejercicio 1
class Producto:
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        print("-------------informacion del producto-------------------")
        print(f"Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}")
    
    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(" -------------------stock actualizado-------------")
        print(f"Stock actualizado: {self.stock} Producto: {self.nombre}")   
    
    def vender(self, cantidad):
        if cantidad > self.stock:
            return "No hay suficiente stock para realizar la venta."
        else:
            self.stock -= cantidad
            total = cantidad * self.precio
            print("----------------Venta realizada ---------------- ")
            print(f"Venta : {cantidad} Unidad {self.nombre}. Total : {total}")
            return total    

print( "\n ---------------------------------------------"  )  

class Tienda:

    def __init__(self, nombre:str, productos:list):
        self.nombre = nombre
        self.productos = productos
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Productos Agregados a la tienda")
        print(f"Producto Nombre :  {producto.nombre} Se agregado a la tienda : {self.nombre}.")
        
    def listar_productos(self):
        print(f"Productos disponibles en {self.nombre}:")
        for producto in self.productos:
         
            print("--------------------------------------------------")
            print(f"- {producto.nombre} (Precio: {producto.precio}, Stock: {producto.stock})")
    
    def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    total = cantidad * producto.precio
                    print(f"Venta realizada: {cantidad} unidades de {producto.nombre}. Total: {total}")
                    return total
                else:
                    print(f"No hay suficiente stock de {producto.nombre}. Stock disponible: {producto.stock}")
                    return None
        print(f"Producto {nombre_producto} no encontrado en la tienda.")
        return None        


if __name__ == "__main__":
# -------------------------------    
    producto1 = Producto("Computador de escritorio", 900, 30)
    producto1.mostrar_info()
# ---------------------
    producto1.actualizar_stock(20)
    producto1.mostrar_info()
    
    total_venta = producto1.vender(9)
    print(f"Total de la venta: {total_venta}")
    
    producto1.mostrar_info()
    
    error_venta = producto1.vender(100)
    print(error_venta)

    # tienda y productos
    producto1 = Producto("Monitor", 150, 20)
    producto2 = Producto("Mouse", 25, 50)
    producto3 = Producto("Teclado", 45, 40)
    producto4 = Producto("pad mouse", 10, 5)
    
    tienda = Tienda("Super Market", [producto1, producto2, producto3, producto4])
    tienda.listar_productos()   
    tienda.agregar_producto(producto3)
    tienda.agregar_producto(producto4)
    tienda.listar_productos()
    tienda.vender_producto("Mouse", 5)
    tienda.vender_producto("Teclado", 100)
    tienda.vender_producto("Monitor", 1)
    