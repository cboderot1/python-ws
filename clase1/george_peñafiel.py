# EJERCICIO: 1

def person():
    name = input("Nombre: ")
    edad = input("Edad: ")
    talla = input("Talla (en metros): ")
    peso = input("Peso (en kilogramos): ")
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
    print("Gracias por usar el programa.")