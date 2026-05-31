# Ejercicio 2: Temperaturas
# Almacena temperaturas de 10 días y calcula: máx, mín, promedio y días > 30°C

def temperaturas():
    temperaturas = []

    print("=== REGISTRO DE TEMPERATURAS (10 DÍAS) ===\n")

    for i in range(1, 11):
        while True:
            try:
                temp = float(input(f"Temperatura día {i}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Ingrese un número válido.")

    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    promedio = sum(temperaturas) / len(temperaturas)
    dias_calurosos = sum(1 for t in temperaturas if t > 30)

    print("\n=== RESULTADOS ===")
    print(f"Temperatura más alta:           {temp_max:.1f}°C")
    print(f"Temperatura más baja:           {temp_min:.1f}°C")
    print(f"Promedio de temperaturas:       {promedio:.1f}°C")
    print(f"Días por encima de 30°C:        {dias_calurosos}")

temperaturas()
