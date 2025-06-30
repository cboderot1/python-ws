# ejercicio 1

def solicitar_datos():
    """Solicito los datos del usuario y los retorna en un diccionario"""
    print("=== CALCULADORA DE IMC ===\n")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    talla = float(input("Talla (m): "))
    peso = float(input("Peso (kg): "))
    
    return {'nombre': nombre, 'edad': edad, 'talla': talla, 'peso': peso}

def calcular_y_clasificar_imc(peso, talla):
    """Calculo el IMC y retorna el valor y su clasificación"""
    imc = round(peso / (talla ** 2), 2)
    
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif 18.5 <= imc <= 24.9:
        clasificacion = "Peso saludable"
    elif 25.0 <= imc <= 29.9:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"
    
    return imc, clasificacion

def mostrar_resultado(datos, imc, clasificacion):
    """Muestro el resultado final del cálculo"""
    print(f"\nHola {datos['nombre']}, tu IMC es {imc}. Tienes {clasificacion.lower()}.")

def main1():
    """Función principal del programa"""
    # Solicitar datos
    datos_usuario = solicitar_datos()
    
    # Calcular IMC y obtener clasificación
    imc, clasificacion = calcular_y_clasificar_imc(datos_usuario['peso'], datos_usuario['talla'])
    
    # Mostrar resultado
    mostrar_resultado(datos_usuario, imc, clasificacion)

def obtener_datos_y_procesar():
    """Solicita números, valida y procesa el intervalo"""
    print("=== NÚMEROS PARES EN UN INTERVALO ===\n")
    
    while True:
        try:
            num1 = int(input("Ingresa el número menor: "))
            num2 = int(input("Ingresa el número mayor: "))
            
            # Validar que sean positivos y que el primero sea menor
            if num1 <= 0 or num2 <= 0:
                print("❌ Los números deben ser positivos. Intenta nuevamente.\n")
                continue
            if num1 >= num2:
                print("❌ El primer número debe ser menor que el segundo. Intenta nuevamente.\n")
                continue
            
            # Procesar el intervalo
            pares = [num for num in range(num1, num2 + 1) if num % 2 == 0]
            total = num2 - num1 + 1
            
            return num1, num2, pares, total
            
        except ValueError:
            print("❌ Por favor ingresa solo números enteros válidos.\n")

def mostrar_resultados(menor, mayor, pares, total):
    """Muestra los resultados del análisis"""
    print(f"\nNúmeros pares entre {menor} y {mayor}:")
    print(", ".join(map(str, pares)))
    print(f"\nCantidad total de números en el intervalo: {total}")

def main2():
    """Función principal del programa"""
    # Obtener datos y procesar
    numero_menor, numero_mayor, numeros_pares, cantidad_total = obtener_datos_y_procesar()
    
    # Mostrar resultados
    mostrar_resultados(numero_menor, numero_mayor, numeros_pares, cantidad_total)

# Ejecutar el programa
if __name__ == "__main__":
    main1()
    main2()
    
    
    