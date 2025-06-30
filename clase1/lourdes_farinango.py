# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 12:58:29 2025

@author: Lourdes Farinango

Ejercicios Clase 1
"""

def ejercicio_imc():
    """
    Ejercicio 1: Calculadora de IMC (Índice de Masa Corporal)
    """
    print("\n=== CALCULADORA DE IMC ===")
    
    # Solicitar datos del usuario
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    talla = float(input("Ingrese su talla (en metros): "))
    peso = float(input("Ingrese su peso (en kilogramos): "))
    
    # Calcular el IMC: IMC = peso / (talla^2)
    imc = peso / (talla ** 2)
    
    # Determinar categoría según el IMC
    if imc < 18.5:
        categoria = "Bajo peso"
    elif 18.5 <= imc <= 24.9:
        categoria = "Peso saludable"
    elif 25.0 <= imc <= 29.9:
        categoria = "Sobrepeso"
    else:  # imc >= 30.0
        categoria = "Obesidad"
    
    # Mostrar resultado
    print(f"\nNombre: {nombre} Edad: {edad} Talla (m): {talla} Peso (kg): {peso}")
    print(f"\nHola {nombre}, tu IMC es {imc:.2f}. Tienes {categoria.lower()}.")


def ejercicio_pares():
    """
    Ejercicio 2: Números pares en un intervalo
    """
    print("\n=== NÚMEROS PARES EN INTERVALO ===")
    
    # Solicitar y validar números
    while True:
        try:
            num_menor = int(input("Ingresa el número menor: "))
            num_mayor = int(input("Ingresa el número mayor: "))
            
            # Validación: números positivos
            if num_menor <= 0 or num_mayor <= 0:
                print("Error: Ambos números deben ser enteros positivos.")
                continue
            
            # Validación: orden correcto
            if num_menor >= num_mayor:
                print("Error: El primer número debe ser menor que el segundo.")
                continue
            
            # Validaciones pasaron
            break
            
        except ValueError:
            print("Error: Ingrese solo números enteros.")
    
    # Encontrar números pares en el rango
    numeros_pares = []
    for numero in range(num_menor, num_mayor + 1):
        if numero % 2 == 0:  # Verificar si es par
            numeros_pares.append(numero)
    
    # Calcular cantidad total de números en el intervalo
    cantidad_total = num_mayor - num_menor + 1
    
    # Mostrar resultados
    pares_str = ", ".join(map(str, numeros_pares))
    print(f"\nNúmeros pares entre {num_menor} y {num_mayor}: {pares_str}")
    print(f"Cantidad total de números en el intervalo: {cantidad_total}")


def mostrar_ayuda():
    """
    Muestra la ayuda del programa con opciones disponibles
    """
    print("=" * 50)
    print("         EJERCICIOS PYTHON - CLASE 1")
    print("=" * 50)
    print()
    print("Opciones disponibles:")
    print("  imc   - Calculadora de Índice de Masa Corporal")
    print("  pares - Encontrar números pares en un intervalo")
    print("  salir - Terminar el programa")
    print()
    print("=" * 50)


def ejecutor_interactivo():
    """
    Función principal que maneja la ejecución interactiva
    """
    # Mostrar ayuda inicial
    mostrar_ayuda()
    
    # Diccionario para mapear opciones a funciones
    opciones = {
        'imc': ejercicio_imc,
        'pares': ejercicio_pares,
    }
    
    # Loop principal de interacción
    while True:
        try:
            print("\n" + "-" * 30)
            opcion = input("Seleccione una opción: ").lower().strip()
            
            if opcion == 'salir':
                print("\n¡Gracias por usar los ejercicios Python de la Clase 1!")
                break
            elif opcion in opciones:
                # Ejecutar la función correspondiente
                opciones[opcion]()
            else:
                print(f"\nOpción '{opcion}' no válida.")
                print("Opciones disponibles: imc, pares, help, salir")
                
        except KeyboardInterrupt:
            # Manejo de Ctrl+C
            print("\n\n¡Programa terminado por el usuario!")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Por favor, intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutor_interactivo()