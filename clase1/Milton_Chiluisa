def solicitar_numeros():
    """
    Solicita al usuario dos números enteros: uno menor y uno mayor.
    Valida que los números sean enteros positivos y que el primer número
    sea estrictamente menor que el segundo.
    """
    while True:
        try:
            # Solicita el primer número, que se espera sea el menor
            num_menor_str = input("Ingresa el número menor: ")
            num_menor = int(num_menor_str)

            # Solicita el segundo número, que se espera sea el mayor
            num_mayor_str = input("Ingresa el número mayor: ")
            num_mayor = int(num_mayor_str)

            # Valida que ambos números sean positivos
            if num_menor < 0 or num_mayor < 0:
                print("Error: Ambos números deben ser enteros positivos. Intenta de nuevo.")
                continue # Vuelve a pedir los números si la validación falla

            # Valida que el primer número sea menor que el segundo
            if num_menor >= num_mayor:
                print("Error: El número menor debe ser estrictamente menor que el número mayor. Intenta de nuevo.")
                continue # Vuelve a pedir los números si la validación falla

            # Si todas las validaciones son exitosas, sale del bucle
            return num_menor, num_mayor

        except ValueError:
            # Captura el error si el usuario no ingresa un número entero válido
            print("Error: Entrada inválida. Por favor, ingresa solo números enteros. Intenta de nuevo.")
        except Exception as e:
            # Captura cualquier otro error inesperado
            print(f"Ocurrió un error inesperado: {e}. Intenta de nuevo.")


def mostrar_numeros_pares(num_menor, num_mayor):
    """
    Recibe un rango de números (num_menor, num_mayor) y muestra
    todos los números pares dentro de ese rango, inclusive.
    """
    numeros_pares = [] # Lista para almacenar los números pares encontrados
    # Itera a través del rango de números, desde num_menor hasta num_mayor (inclusive)
    for numero in range(num_menor, num_mayor + 1):
        # Comprueba si el número es par (el residuo de la división por 2 es 0)
        if numero % 2 == 0:
            numeros_pares.append(numero) # Añade el número par a la lista

    # Convierte la lista de números pares a una cadena de texto para mostrarla
    # Se utiliza un generador para convertir cada número a string antes de unir
    pares_str = ', '.join(str(n) for n in numeros_pares)
    print(f"Números pares entre {num_menor} y {num_mayor}: {pares_str}")


def calcular_cantidad_total(num_menor, num_mayor):
    """
    Recibe un rango de números (num_menor, num_mayor) y calcula
    la cantidad total de números en ese intervalo, inclusive.
    """
    # La cantidad total de números en un rango inclusivo [a, b] es (b - a + 1)
    cantidad = num_mayor - num_menor + 1
    print(f"Cantidad total de números en el intervalo: {cantidad}")


# --- Bloque principal de ejecución del programa ---
if __name__ == "__main__":
    print("--- Calculadora de Rango de Números ---")
    # Llama a la función para solicitar y validar los números
    numero1, numero2 = solicitar_numeros()

    # Muestra los números pares en el rango validado
    mostrar_numeros_pares(numero1, numero2)

    # Calcula y muestra la cantidad total de números en el rango validado
    calcular_cantidad_total(numero1, numero2)

    print("\n--- Programa finalizado ---")
    print("Este es mi cambio para el deber de programación")
    print("Este es mi primer cambio para el deber")
    
