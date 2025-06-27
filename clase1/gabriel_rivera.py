# Calculadora de IMC y Números Pares
# Versión: 1.00
# Autor: Gabriel Rivera
# Fecha: 2025-06-26

def calculadora_imc():
    """
    Ejercicio 1: Calculadora de IMC (Índice de Masa Corporal)
    """
    print("=== CALCULADORA DE IMC ===")
    
    # Paso 1: Solicitar datos del usuario
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    talla = float(input("Ingrese su talla (en metros): "))
    peso = float(input("Ingrese su peso (en kilogramos): "))
    
    # Paso 2: Calcular el IMC
    # Fórmula: IMC = peso / (talla^2)
    imc = peso / (talla ** 2)
    
    # Paso 3: Determinar la categoría según el IMC
    if imc < 18.5:
        categoria = "Bajo peso"
    elif 18.5 <= imc <= 24.9:
        categoria = "Peso saludable"
    elif 25.0 <= imc <= 29.9:
        categoria = "Sobrepeso"
    else:  # imc >= 30.0
        categoria = "Obesidad"
    
    # Paso 4: Mostrar el resultado de acuerdo a Salida Espera
    print(f"\nNombre: {nombre} Edad: {edad} Talla (m): {talla} Peso (kg): {peso}")
    print(f"\nHola {nombre}, tu IMC es {imc:.2f}. Tienes {categoria.lower()}")


def validar_numero_positivo(numero):
    """
    Valida que un número sea entero positivo
    
    Args:
        numero (int): Número a validar
        
    Returns:
        bool: True si es positivo, False si no
    """
    return numero > 0


def numeros_pares_intervalo():
    """
    Ejercicio 2: Encuentra números pares en un intervalo
    """
    print("=== NÚMEROS PARES EN INTERVALO ===")
    
    # Paso 1: Solicitar y validar números
    while True:
        try:
            num_menor = int(input("Ingresa el número menor: "))
            num_mayor = int(input("Ingresa el número mayor: "))
            
            # Validación 1: Números positivos
            if not (validar_numero_positivo(num_menor) and validar_numero_positivo(num_mayor)):
                print("Error: Ambos números deben ser enteros positivos.")
                continue
            
            # Validación 2: Orden correcto
            if num_menor >= num_mayor:
                print("Error: El primer número debe ser menor que el segundo.")
                continue
            
            # Si llegamos aquí, las validaciones pasaron
            break
            
        except ValueError:
            print("Error: Ingrese solo números enteros.")
    
    # Paso 2: Encontrar números pares en el rango
    numeros_pares = []
    for numero in range(num_menor, num_mayor + 1):  # +1 para incluir el límite superior
        if numero % 2 == 0:  # Verificar si es par
            numeros_pares.append(numero)
    
    # Paso 3: Calcular cantidad total de números en el intervalo
    cantidad_total = num_mayor - num_menor + 1
    
    # Paso 4: Mostrar resultados
    pares_str = ", ".join(map(str, numeros_pares))
    print(f"\nNúmeros pares entre {num_menor} y {num_mayor}: {pares_str}")
    print(f"Cantidad total de números en el intervalo: {cantidad_total}")


def main():
    """
    Función principal con menú de opciones
    """
    print("=== EJERCICIOS PYTHON CLASE 1 ===")
    print("1. Calculadora de IMC")
    print("2. Números pares en intervalo")
    
    while True:
        try:
            opcion = int(input("\nSeleccione una opción (1 o 2): "))
            
            if opcion == 1:
                calculadora_imc()
                break
            elif opcion == 2:
                numeros_pares_intervalo()
                break
            else:
                print("Opción inválida. Ingrese 1 o 2.")
                
        except ValueError:
            print("Error: Ingrese un número válido.")


# Ejecutar el programa
if __name__ == "__main__":
    main()