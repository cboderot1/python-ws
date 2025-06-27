# Ejerccio 2 Boris Guerra
# definicion de ingreso de numeros
def solicitar_numeros():
    menor = int(input("Ingresa el número menor: "))
    mayor = int(input("Ingresa el número mayor: "))
    while menor >= mayor:
        print("El primer valor debe ser un numero menor que el segundo valor ingresa de nuevo")
        menor = int(input("Ingresa el número menor: "))
        mayor = int(input("Ingresa el número mayor: "))
    return menor, mayor
# visualiza los numeros en un rango
def mostrar_numeros(menor, mayor):
    print(f"\nNúmeros entre {menor} y {mayor}:")
    print(", ".join(str(num) for num in range(menor, mayor + 1)))
# numeros pares en un rango
def numeros_pares_rango(menor, mayor):
    return [num for num in range(menor, mayor + 1) if num % 2 == 0]

# vsualizo cantida total de numeros en un rango
def cantidad_total(menor, mayor):
    return mayor - menor + 1


def main():
    menor, mayor = solicitar_numeros()
    mostrar_numeros(menor, mayor)
    
    pares = numeros_pares_rango(menor, mayor)
    total = cantidad_total(menor, mayor)

    print(f"\nNúmeros pares entre {menor} y {mayor}:")
    print(", ".join(map(str, pares)))

    print(f"\nCantidad total de números en el intervalo: {total}")


#llamo a la funcion de ejecucion main
if __name__ == "__main__":
    main()
    