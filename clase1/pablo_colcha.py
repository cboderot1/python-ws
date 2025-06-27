#ejercicio 1

def person():
    name = input("Ingrese su Nombre: ")
    edad = input("Ingrese su Edad: ")
    talla = input("Talla (ejemplo: 1.65): ")
    peso = input("Peso (ejemplo: 65 Kg): ")
    return name, edad, talla, peso
    
def calcular_imc(peso, talla):
    peso = float(peso)
    talla = float(talla)
    return peso/(talla**2)

def clasificar_imc(imc):
    if (imc < 18.5): 
        mensaje = "Bajo peso"
    elif (imc < 25):
        mensaje = "Peso saludable"
    elif (imc < 30):
        mensaje = "Sobrepeso"    
    else:
        mensaje = "Obesidad"
    return mensaje

def ejercicio1(peso, talla):
    imc = calcular_imc(peso, talla)
    mensaje = clasificar_imc(imc)
    return mensaje


if __name__ == "__main__":
    name, edad, talla, peso = person()
    
    msn = ejercicio1(peso, talla)

    print(f"Hola {name} tienes {edad} años y estas en: {msn}")
    
    
    
#ejercicio 2
    
#funcion solicitar_numeros
def solicitar_numeros():
    while True:
        try:
            # Solicitar al usuario que ingrese dos números
            n1 = int(input("Ingrese el primer número (menor): "))
            n2 = int(input("Ingrese el segundo número (mayor): "))
            # Validar que ambos números sean enteros y positivos
            if n1 <= 0 or n2 <= 0:
                print("Ambos números deben ser enteros positivos.")
                continue
            if n1 >= n2:
                print("El primer número debe ser menor que el segundo.")
                continue

            return n1, n2
        # Manejar excepciones
        except ValueError:
            print("Por favor, ingrese solo números enteros válidos.")

#funcion mostrar_pares y conteo
def mostrar_pares_y_conteo(n1, n2):
    pares = []
    # Calcular los números pares entre n1 y n2
    for num in range(n1, n2 + 1):
        if num % 2 == 0:
            pares.append(num)
            total=len(pares)
    # Mostrar los números pares y el conteo
    print(f"Números pares entre {n1} y {n2}: {pares}")
    print(f"Cantidad total de números en el rango: {total}")
# Programa principal
if __name__ == "__main__":
    n1, n2 = solicitar_numeros()
    mostrar_pares_y_conteo(n1, n2)
    
    