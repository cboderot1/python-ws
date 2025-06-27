#
# EJERCICIO 1: Calculadora de IMC
#

# Datos del usuario
nombre = input("¿Cuál es tu nombre?")
edad = int(input("¿Cuántos años tienes?"))
talla = float(input("¿Cuál es tu talla en metros? (ej. 1.70):"))
peso = float(input("¿Cuál es tu peso en kilogramos? (ej. 65):"))

# Cálculo del IMC
imc = peso / (talla ** 2)

# Resultado del usuario con dos decimales
print(f"\nHola {nombre}, tu IMC es: {imc:.2f}")

# Mensaje según el valor del IMC
if imc < 18.5:
    print("Tienes bajo peso.")
elif 18.5 <= imc <= 24.9:
    print("Tienes un peso saludable.")
elif 25.0 <= imc <= 29.9:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad")

#
# EJERCICIO 2: Números pares en un intervalo
#

# Solicita dos números enteros
while True:
    try:
        num_menor = int(input("Ingresa un número entero menor"))
        num_mayor = int(input("Ingresa un número entero mayor"))

        if num_menor < num_mayor:
            break
        else:
            print("El primer núemro debe ser menor que el segundo. Intenta de nuevo.\n")
    except ValueError:
        print("Por favor, ingresa solo números enteros.\n")

# Muestra todos los números pares en ese rango
print(f"\nNúmeros pares entre {num_menor} y {num_mayor} :")
pares = []
for i in range(num_menor, num_mayor + 1):
    if i % 2 == 0:
        pares.append(i)
        print(i, end=" ")

# Cantidad total de números en el rango
cantidad_total = num_mayor - num_menor + 1

print(f"\n\nCantidad total de números en el rango: {cantidad_total}")
