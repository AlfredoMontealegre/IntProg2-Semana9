"""
3. Promedio de calificaciones
✓ Solicita al usuario 8 calificaciones, guárdalas en una lista y calcula el
promedio.
"""

calificaciones = []

print("Ingresa 8 calificaciones:")

# Pedir 8 calificaciones al usuario
for i in range(8):
    nota = float(input(f"Ingrese la calificación #{i + 1}: "))
    calificaciones.append(nota)

# Calcular el promedio
promedio = sum(calificaciones) / len(calificaciones)

# Mostrar la lista y el promedio
print("\nCalificaciones ingresadas:")
print(calificaciones)

print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")