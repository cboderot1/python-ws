#Programa para calcular el indice de masa corporal
#Klever curay

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def interpretar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso saludable"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    print("Calculadora de Índice de Masa Corporal (IMC)")
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    
    try:
        talla = float(input("Ingresa tu talla en metros (por ejemplo, 1.75): "))
        peso = float(input("Ingresa tu peso en kilogramos: "))
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos para talla y peso.")
        return

    if talla <=0:
       print("Valor de la talla es invalido.")
       return
       
    if peso <=0:
       print("Valor del peso es invalido.")
       return
       
    imc = calcular_imc(peso, talla)
    imc_redondeado = round(imc, 2)
    categoria = interpretar_imc(imc_redondeado)

    print(f"\nHola {nombre}, tu IMC es {imc_redondeado}.")
    print(f"Tienes \"{categoria}\"")

if __name__ == "__main__":
    main()

