################################################
# Calculadora de Índice de Masa Corporal (IMC)
# WALTER NUÑEZ ZAMORA 
#############################################
# Solicitud de datos al usuario
nombre = input("Nombre: ")
edad = int(input("Edad: "))
talla = float(input("Talla (m): "))
peso = float(input("Peso (kg): "))

# Cálculo del IMC
imc = peso / talla**2

# Determinar categoría de peso
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc <= 24.9:
    categoria = "Peso saludable"
elif 25.0 <= imc <= 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

# Mostrar resultado
print(f"\nHola {nombre}, tu IMC es {imc:.2f}.")
print(f"Tienes un {categoria.lower()}.")



################################
# segundo ejemplo 
# Ejercicio 2: Números pares en un intervalo

# Función para validar que los números sean enteros positivos y que el primero sea menor que el segundo
def validar_numeros(menor, mayor):
    return menor >= 0 and mayor >= 0 and menor < mayor

# Función para obtener números pares en un rango dado
def numeros_pares_rango(menor, mayor):
    return [num for num in range(menor, mayor + 1) if num % 2 == 0]

# Solicitar los números al usuario
menor = int(input("Ingresa el número menor: "))
mayor = int(input("Ingresa el número mayor: "))

# Validación de los números ingresados
if validar_numeros(menor, mayor):
    # Obtener números pares
    pares = numeros_pares_rango(menor, mayor)

    # Mostrar resultados
    print(f"\nNúmeros pares entre {menor} y {mayor}:")
    print(", ".join(map(str, pares)))

    total_numeros = mayor - menor + 1
    print(f"\nCantidad total de números en el intervalo: {total_numeros}")
else:
    print("\nError: Asegúrate de ingresar números enteros positivos y que el primero sea menor que el segundo.")