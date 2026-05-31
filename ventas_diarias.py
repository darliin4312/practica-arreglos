# Ejercicio 1: Ventas Diarias
# Registra ventas de 7 días y calcula: total, promedio y día con venta máxima

def ventas_diarias():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    ventas = []

    print("=== REGISTRO DE VENTAS SEMANALES ===\n")

    for i in range(7):
        while True:
            try:
                venta = float(input(f"Ingrese las ventas del {dias[i]}: $"))
                if venta < 0:
                    print("Error: La venta no puede ser negativa.")
                else:
                    ventas.append(venta)
                    break
            except ValueError:
                print("Error: Ingrese un número válido.")

    total = sum(ventas)
    promedio = total / 7
    max_venta = max(ventas)
    dia_max = dias[ventas.index(max_venta)]

    print("\n=== RESULTADOS ===")
    print(f"Total vendido en la semana: ${total:.2f}")
    print(f"Promedio diario:            ${promedio:.2f}")
    print(f"Día con mayor venta:        {dia_max} (${max_venta:.2f})")

ventas_diarias()
