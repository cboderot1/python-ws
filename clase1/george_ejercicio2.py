
def obtener_numeros_del_usuario():
    
    while True:
        try:
            
            numero_menor = int(input("Ingrese el número MENOR: "))
            numero_mayor = int(input("Ingrese el número MAYOR: "))
            
            if numero_menor >= numero_mayor:
                print("¡Error! El primer numero debe se menor que el segundo. Intenténtelo de nuevo.")
                continue
            
            if numero_menor < 0 or numero_mayor <= 0:
                print("¡Error! Por favor, ingresa números enteros positivos. Intenténtelo de nuevo.")
                continue
            
            return numero_menor, numero_mayor
        
        except ValueError:
            print("¡Error! Por favor, ingresa solo números enteros. Inténtalo de nuevo. Intenténtelo de nuevo.")

def encontar_numeros_pares(inicio, fin):
    
    numeros_pares = []
    
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            numeros_pares.append(numero)
            
        numeros_pares_str = ', '.join(map(str, numeros_pares))
        print(f"Números pares entre {inicio} y {fin} son: {numeros_pares_str}")
        
def contar_total_numeros(inicio, fin):
    
    total_numeros = fin - inicio + 1
    
    print(f"Cantidad total de números en el intervalo: {total_numeros}") 
    
if __name__ == "__main__":
    numero_menor, numero_mayor = obtener_numeros_del_usuario()
    
    encontar_numeros_pares(numero_menor, numero_mayor)
    
    contar_total_numeros(numero_menor, numero_mayor)