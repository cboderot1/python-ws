# Programa para obtenre los numeros pares de un rango ingresado
# Klever Curay

def solicitar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero <= 0:
                print("Por favor, ingresa un número entero positivo.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

def main():
    print("Ingresa dos números enteros positivos:")

    menor = solicitar_numero("Número menor: ")
    mayor = solicitar_numero("Número mayor: ")

    while menor >= mayor:
        print("El primer número debe ser menor que el segundo.")
        menor = solicitar_numero("Número menor: ")
        mayor = solicitar_numero("Número mayor: ")

    # Números pares en el rango (inclusive)
    pares = [num for num in range(menor, mayor + 1) if num % 2 == 0]

    # Cantidad total de números en el intervalo
    total = (mayor - menor) + 1

    # Mostrar resultados
    print(f"\nNúmeros pares entre {menor} y {mayor}:")
    print(", ".join(map(str, pares)))
    print(f"\nCantidad total de números en el intervalo: {total}")

if __name__ == "__main__":
    main()

