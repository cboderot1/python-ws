# Ejercicio 1

def ejercicio1 (peso,talla):
    peso = float(peso)
    talla = float(talla)
    imc = peso/(talla**2)
    if imc < 18.5:
        mensaje = "Tiene un peso Bajo"
    elif imc >= 18.5 and imc < 24.9:
        mensaje = "Tiene un peso Saludable"
    elif imc >= 25 and imc < 29.9:
        mensaje = "Tiene Sobrepeso"
    else:
        mensaje = "Tiene Obesidad"
    return mensaje
#Ejercicio 2

def ejercicio2 (n_menor, n_mayor):
    n_menor = int(n_menor)
    n_mayor = int(n_mayor)
    pares = []
    if n_menor < n_mayor:
        for i in range (n_menor,n_mayor +1):
            if i% 2 == 0:
                pares.append(i)
        intervalo = n_mayor-n_menor+1       
        return pares, intervalo
    else:
        mensaje= "El segundo numero debe de ser mayor "
        return mensaje


if __name__ == "__main__":

    # Ejercicio 2
    n_menor = input("Ingresa el numero menor: ")
    n_mayor = input("Ingresa el numero mayor: ")
    print (f"Numeros pares entre {n_menor} y {n_mayor} son: ")    
    
    numeros,intervalo= ejercicio2(n_menor, n_mayor)

    print(f"Numeros pares entre {n_menor} y {n_mayor} son: {numeros}")
    print(f"Cantidad total de números en el intervalo: {intervalo}")