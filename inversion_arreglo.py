# Ejercicio 3: Inversión de Arreglo
# Almacena 6 números e imprime el arreglo en orden inverso

def inversion_arreglo():
    numeros = []

    print("=== INVERSIÓN DE ARREGLO ===\n")
    print("Ingrese 6 números:")

    for i in range(1, 7):
        while True:
            try:
                num = float(input(f"Número {i}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Error: Ingrese un número válido.")

    print(f"\nArreglo original: {numeros}")

    arreglo_invertido = numeros[::-1]

    print(f"Arreglo invertido: {arreglo_invertido}")

inversion_arreglo()
