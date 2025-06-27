# Ejercicio 1 Boris Guerra
def ejercicio1():
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    peso = float(input("Introduce tu peso en kg: "))
    talla = float(input("Introduce tu talla en metros: "))
    imc = calcular_imc(peso, talla)
    mostrar_resultado(imc)

def calcular_imc(peso, talla):
    return peso / (talla ** 2)

def mostrar_resultado(imc):
    print(f"Tu IMC es: {imc:.2f}")
    if imc < 18.5:
        print("Bajo peso")
    elif 18.5 <= imc <= 24.9:
        print("Peso saludable")
    elif 25.0 <= imc <= 29.9:
        print("Sobrepeso")
    else:
        print("Obesidad")



if __name__ == "__main__":
    ejercicio1()