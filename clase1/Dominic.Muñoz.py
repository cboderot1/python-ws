"""
## 🔢 Ejercicio 2: Números pares en un intervalo

### 📌 Requisitos:
- Solicita dos números enteros: uno menor y uno mayor.
- Valida que el primer número sea menor que el segundo.
- Validar que sean números enteros positivos.
- Muestra:
- Todos los números pares en ese rango (inclusive)
- La cantidad total de números en ese rango

### ✅ Salida esperada:
"""
def solicitar_numeros():
    """Solicita dos números enteros positivos y valida que el primero sea menor que el segundo."""
    while True:
        try:
            num1 = int(input("Ingrese el primer número (entero positivo): "))
            num2 = int(input("Ingrese el segundo número (entero positivo): "))

            if num1 <= 0 or num2 <= 0:
                print("❌ Ambos números deben ser enteros **positivos**.\n")
            elif num1 >= num2:
                print("❌ El primer número debe ser **menor** que el segundo.\n")
            else:
                return num1, num2
        except ValueError:
            print("❌ Entrada no válida. Debe ingresar números **enteros**.\n")

def obtener_pares(num1, num2):
    """Retorna una lista de números pares dentro del rango """
    return [i for i in range(num1, num2 + 1) if i % 2 == 0]

def contar_total_numeros(num1, num2):
    """Retorna la cantidad total de números en el rango"""
    return num2 - num1 + 1

def mostrar_resultados(pares, total):
    """Muestra los resultados en pantalla."""
    print("\n✅ Números pares en el rango:")
    print(pares)
    print(f"\n📊 Cantidad total de números en el rango: {total}")

def main():
    num1, num2 = solicitar_numeros()
    pares = obtener_pares(num1, num2)
    total = contar_total_numeros(num1, num2)
    mostrar_resultados(pares, total)

# Ejecutar el programa
main()
