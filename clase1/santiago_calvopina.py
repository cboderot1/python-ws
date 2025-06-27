# /////////////////////////////////////////
# Clase Persona: para calculo del IMC
# /////////////////////////////////////////
class Persona:
    def __init__(self, nombre, edad, talla, peso):
        self.nombre = nombre
        self.edad = edad
        self.talla = talla
        self.peso = peso

    def calcular_imc(self):
        imc = self.peso / (self.talla ** 2)

        print("\n--- RESULTADO IMC ---")
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nTalla(m): {self.talla}\nPeso(kg): {self.peso}")

        if imc < 18.5:
            mensaje = "Estás bajo de peso"
        elif 18.5 <= imc <= 24.9:
            mensaje = "Tienes un peso saludable"
        elif 25.0 <= imc <= 29.9:
            mensaje = "Tienes sobrepeso"
        else:
            mensaje = "Tienes obesidad"

        print(f"{self.nombre}, tu IMC es {imc:.2f}. {mensaje}.")

# /////////////////////////////////////////
# Clase RangoNumeros: números pares
# /////////////////////////////////////////
class RangoNumeros:
    def __init__(self, numMenor, numMayor):
        self.numMenor = numMenor
        self.numMayor = numMayor

    def obtener_pares(self):
        pares = [num for num in range(self.numMenor, self.numMayor + 1) if num % 2 == 0]
        return pares

    def cantidad_total(self):
        return self.numMayor - self.numMenor + 1

# /////////////////////////////////////////
# Función para calcular IMC
# /////////////////////////////////////////
def ejecutar_calculo_imc():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    talla = float(input("Ingrese su talla en metros: "))
    peso = float(input("Ingrese su peso en kilogramos: "))

    persona = Persona(nombre, edad, talla, peso)
    persona.calcular_imc()

# /////////////////////////////////////////
# Función para calcular rango de números pares
# /////////////////////////////////////////
def ejecutar_numeros_pares():
    while True:
        try:
            numMenor = int(input("Ingresa el número menor: "))
            numMayor = int(input("Ingresa el número mayor: "))
            
            if numMenor < 0 or numMayor < 0:
                print("⚠️ Los números deben ser enteros positivos.")
            elif numMenor >= numMayor:
                print("⚠️ El primer número debe ser menor que el segundo.")
            else:
                break
        except ValueError:
            print("⚠️ Ingresa solo números enteros.")

    rango = RangoNumeros(numMenor, numMayor)
    pares = rango.obtener_pares()
    total = rango.cantidad_total()

    print(f"\nNúmeros pares entre {numMenor} y {numMayor}: {', '.join(map(str, pares))}")
    print(f"Cantidad total de números en el intervalo: {total}")

# /////////////////////////////////////////
# Llamar funciones 
# /////////////////////////////////////////
if __name__ == "__main__":
    ejecutar_calculo_imc()
    ejecutar_numeros_pares()