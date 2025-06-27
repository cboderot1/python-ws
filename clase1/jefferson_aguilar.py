# EJERCICIO 1

def ejercicio1(peso, talla):
    peso = float(peso)
    talla = float(talla)
    imc = peso/(talla*talla)
    if (imc < 18.5):
        mensaje = " es Bajo"
    elif (imc < 25):
        mensaje = " es Saludable"
    elif (imc < 30):
        mensaje = "es Sobrepeso"
    else:
        mensaje = " es Obesidad"
    return mensaje


if __name__ == "__main__":

    name = input("El Nombre es: ")
    edad = input("La Edad es: ")
    peso = input("El Peso en kg. es: ")
    talla = input("La Talla m. es: ")
    msn = ejercicio1(peso, talla)
    print(f"Hola {name}, tienes {edad} años y tu peso es {msn}")

  #  Ejercicio2()

def obtener_numero(mensaje):
    numero = input(mensaje) 
    return int(numero)  

def numeros_pares_en_rango(minimo, maximo):
    pares = [] 
    for num in range(minimo, maximo + 1): 
        if num % 2 == 0:
            pares.append(num) 
    return pares

def main():
    menor = obtener_numero("Ingresa el número menor: ")
    mayor = obtener_numero("Ingresa el número mayor: ")

    if menor >= mayor:
        print("El primer número debe ser menor que el segundo.")
        return 

    pares = numeros_pares_en_rango(menor, mayor)

    print("Números pares entre", menor, "y", mayor, ":")
    for p in pares:
        print(p, end=", ") 

    cantidad_total = mayor - menor + 1
    print("\nCantidad total de números en el intervalo:", cantidad_total)

main()


##TEST